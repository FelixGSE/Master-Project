# ----
# Parameter transformation function
# ----

logit <- function (x, lower=0, upper=1) {
    # checking if x is too close to boundaries
    epsilon <- 1e-15
    x <- ifelse(x == upper, upper - epsilon, 
         ifelse(x == lower, lower + epsilon, x))
    
    # rescaling
    log( (x - lower)/(upper - x) )
}

expit <- function (p, lower=0, upper=1) {
    p[p > 700] <- 700  # checking if p is too close to boundaries
    (exp(p)*upper + lower) / (1+exp(p))
}


ident <- function(x) {
    x
}


transformPars <- function(parameters, transformFncs) {

    # check if parameters is a vector, if yes convert to a matrix
    if(is.null(dim(parameters))) {
        parameters <- matrix(parameters, nrow=1)
    }

    # transforming the parameters according to the transformFncs argument
    for(i in 1:ncol(parameters)) {
        # print(names(transformFncs)[i])
        switch(names(transformFncs)[i],
               ident = {parameters[,i] <- ident(parameters[,i])},
               logit = {parameters[,i] <- logit(parameters[,i], transformFncs[[i]][[1]], transformFncs[[i]][[2]])},
               log = {parameters[,i] <- log(parameters[,i])}
               )
    }
    return(parameters)
}

transformParsBack <- function(pars, transformFncs) {
    # assert equal lengths
    stopifnot(length(pars)==length(transformFncs))
    for(i in 1:length(transformFncs)) {
        switch(names(transformFncs)[[i]],
               logit = {pars[i] <- expit(pars[i],transformFncs[[i]][[1]], transformFncs[[i]][[2]])},
               log = {pars[i] <- exp(pars[i])},
               identity = {pars[i] <- identity(pars[i])}
               )
    }
    return(pars)
}



numToProb <- function(numVector) {

    # This function transforms an arbitrary vector of real numbers of length k to vector of real numbers of length k+1 where numbers are in [0,1] interval and they sum to 1. This is particularly useful for optimization or estimation of parameters when paramaters have to sum to 1, but we do not want to estimate all n parameters, but n-1 paramaters instead.

    # Ensure numbers from numVector are in [0,1]
    numVector <- 1/(1+exp(-numVector))

    # Ensure that transformed numbers add up to 1
    if(length(numVector)>1) {
        newVector <- numVector[1]
        for(i in 2:length(numVector)){
          newVector <- c(newVector, numVector[i]*(1-sum(newVector[1:(i-1)])))
        }
        numVector <- newVector
    }
    
    # adding the final parameter that we do not need to estimate
    probVector <- c(numVector, 1-sum(numVector))

    return(probVector)
}

# for those models that used numToProb we have to use it again on every result
backToProb <- function(results, begin, end) {
    for (r in 1:nrows(results)) {
        tmp <- numToProb(as.numeric(results[r, begin:end]))
        results[r, begin:(end+1)] <- tmp
    }
    return(results)
}
