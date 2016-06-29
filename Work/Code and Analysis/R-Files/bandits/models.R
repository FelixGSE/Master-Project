
# ----------------------------------------------------------------------
# Expectancy learning models
# ----------------------------------------------------------------------


delta <- function(eta, choices, utility, noArms) {

        # eta = learning rate
        # choices = vector of agents choices
        # utility = feedback or payoff, potentially transformed via some utility function

        noTrials <- length(choices)
        expValue <- matrix(0.0, nrow=noTrials, ncol=noArms)

        for(trial in 1:(noTrials-1)) {
                expValue[trial+1,] <- expValue[trial,] + 
                        eta*(choices[trial]==1:noArms)*(utility[trial] - expValue[trial,])
        }
        return(expValue)
}

decay <- function(eta, choices, utility, noArms) {

        # from Ahn et al 2008 - a bit strange rule, no asymptote so it could go to infinity...

        # eta = forgetting rate
        # choices = vector of agents choices
        # utility = feedback or payoff, potentially transformed via some utility function

        noTrials <- length(choices)
        expValue <- matrix(0.0, nrow=noTrials, ncol=noArms)
        for(trial in 1:(noTrials-1)) {
                expValue[trial+1,] <- eta*expValue[trial,] + (choices[trial]==1:noArms)*utility[trial]
        }
        return(expValue)
}


# ----------------------------------------------------------------------
# Decision models
# ----------------------------------------------------------------------


softMax <- function(theta, beta=0, expValue) {
    # theta = a temperature parameter
    # beta = a (fixed) bias/exploration "bonus"
    probChoice <- exp(theta*expValue + beta)
    probChoice <- probChoice/rowSum(probChoice) 
    return(probChoice)
}


# ---------------------------------------------------------------------- 
# Objective functions
# ----------------------------------------------------------------------


delta_SM_nLL <- function(par, data, modelVersion, 
                         goal="optimize", 
                         test=FALSE, 
                         verbose=FALSE) {
    
    # storing all the useful data from the model, if in simulate mode
    modelData <- list()
    
    # version specific paremeters
    switch(modelVersion, 
        delta_SM = {  
            eta <- expit(par[1])
            theta <- exp(par[2])
            beta <- 0
        },
        delta_SMb = {  
            eta <- expit(par[1])
            theta <- exp(par[2])
            beta  <- exp(par[3])
        },
        stop("Error: model version not found!")
    )

    # extracting relevant data
    noObs <- nrows(data)
    noArms <- 20
    choices <- data$chosenArm 
    rewards <- data$reward

    # computing the components of the model and finally getting the choice probabilities
    expValue <- delta(eta, choices, utility=rewards, noArms)
    probChoice <- softMax(theta, beta, expValue)

    # choice log likelihood
    ML <- probChoice[cbind(1:noObs,choices)]
    negLogLik <- -sum(log(ML))

    # if there were numerical problems due to exponentiation or division with zero we return infinitely high number so that optimization does not go to that region of the parameter space
    if(is.na(negLogLik)) negLogLik <- Inf

    # store model info after the training
    if (goal=="simulate") {
        modelData$name <- modelVersion
        modelData$train$probChoice <- probChoice 
        modelData$train$probChosen <- ML
        modelData$train$nLL <- negLogLik
        modelData$train$LLt <- exp(-negLogLik/noObs)
        modelData$train$BICt <- exp( (-negLogLik - (length(par)/2)*log(noObs))/noObs )
    }

    if (goal=="optimize") {
        return(negLogLik)
    } else if (goal=="simulate") {
        return(modelData)
    }
}


# ----------------------------------------------------------------------
# Optimization function wrapper
# ----------------------------------------------------------------------

genParGrid <- function(lower, upper, noInitPoints=50) {
    parsInit <- t(fOptions::runif.sobol(noInitPoints,length(lower),1,0,123345))
    parsInit <- t(lower + (upper - lower)*parsInit)
    return(parsInit)
}


optfun <- function(objectiveFunction, lower, upper, transformFncs, modelVersion, data, noOptimInit=3, noInitPoints=50, maxit=200) {
    
    # creating grid of parameter initial points
    parsInit <- genParGrid(lower, upper, noInitPoints)

    # transforming the parameters according to the transformFncs argument
    parsInit <- transformPars(parsInit, transformFncs)

    # computing log likelihoods for all the sets of initial parameters and choose the best or several best ones
    objFunctionValue_Initial <- rep(NA, noInitPoints)
    for(i in 1:noInitPoints) { 
        #print(i)
        objFunctionValue_Initial[i] <- 
        tryCatch({
            objectiveFunction(par=parsInit[i,],data=data, modelVersion=modelVersion)
        }, warning = function(w) {
            #message("Parameters are causing model failure!")
            #message("Here's the original warning #message:")
            #message(w)
            #message("Returning infinity instead!")
            Inf
        }, error = function(e) {
            #message("Parameters are causing model failure!")
            #message("Here's the original error #message:")
            #message(e)
            #message("Returning infinity instead!")
            Inf
        })
    }

    # we choose the best ones, how many depends on 'noOptimInit' parameters
    parsInitBest <- parsInit[which(objFunctionValue_Initial %in% sort(objFunctionValue_Initial)[1:noOptimInit]),]
    if(nrows(parsInitBest)==1) parsInitBest <- matrix(parsInitBest, ncol=1)
    
    # running the optimization based on parsInitBest
    optimResult <- foreach(optimRun = 1:noOptimInit) %do% {
        tryCatch({
            optim(par=parsInitBest[optimRun,], 
                  fn=objectiveFunction, data=data, modelVersion=modelVersion, 
                  control=list(maxit=maxit))
        }, warning = function(w) {
            #message("Parameters are causing model failure!")
            #message("Here's the original warning #message:")
            #message(w)
            #message("Returning infinity instead!")
            list(par=NULL, value=Inf, counts=NULL, convergence=NULL, message=NULL)
        }, error = function(e) {
            #message("Parameters are causing model failure!")
            #message("Here's the original error #message:")
            #message(e)
            #message("Returning infinity instead!")
            list(par=NULL, value=Inf, counts=NULL, convergence=NULL, message=NULL)
        })
    }

    # choose the best one, according to nLL
    negLogLiks <- sapply(1:length(optimResult), function(x) optimResult[[x]]$value)
    optimResult <- optimResult[[which.min(negLogLiks)]]
    return(optimResult)  
}


