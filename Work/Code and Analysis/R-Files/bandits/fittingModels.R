# ----------------------------------------------------------------------
# Information
# ----------------------------------------------------------------------

# This script fits the models to data from the training phase data. Parameters fitted this way will be used to make predictions in the test phase. Performance in the hold out sample - test data - will be a criterion for the model selection.


# ----------------------------------------------------------------------
# Loading data
# ----------------------------------------------------------------------

rm(list = ls())


# Import packages and functions
if (!require("dplyr")) install.packages("dplyr"); library(dplyr)
if (!require("doMC")) install.packages("doMC"); library(doMC)


server = TRUE
if (server) {  # slightly different setup if we run it on a server
    
    # name of the final output file
    saveFileName <- "resultsModeling.RData" 
    noCores <- detectCores() - 2

    # defining the loading name
    loadName <- paste0("banditData.RData")

} else {  # local computer

    setwd("/home/hrvoje/Desktop/test")
    noCores <- detectCores() - 1

    # name of the final ouput file
    saveFileName <- "../dProcessed/resultsModeling.RData"

    # defining the loading name
    loadName <- paste0("../dProcessed/banditData.RData")
}

# loading the data
load(loadName)

# loading functions
source("models.R")
source("usefulFunctions.R")
source("parTransformFunctions.R")
source("initialParameters.R")


# ----------------------------------------------------------------------
# Preparing the data and defining optimization pars
# ----------------------------------------------------------------------

# define optimization parameters
noOptimInit <- 3
noInitPoints <- 1000
maxit <- 400

# preparing the data file
data_MAB <-  filter(taskData, phase == "training")

# list of all su../dProcessedbjects
subjects_MAB <- unique(data_MAB$subjectID)


# data_MAB <- filter(data_MAB, subjectID %in% c("e1-0005"))
# subjects_MAB <- unique(data_MAB$subjectID)


# ----------------------------------------------------------------------
# Fitting models
# ----------------------------------------------------------------------


# define what else to add to the optimization results
getSummary <- function(data, modelName, optimResults, subject, parSpecs) {
    expID <- filter(data, subjectID==subject)$expID[1]
    expCond <- filter(data, subjectID==subject)$expCond[1]
    pars <- rep(NA, 10)
    parNames <- rep(NA, 10)
    noPars <- length(optimResults$par)
    if(noPars!=0) {
        pars[1:noPars] <- transformParsBack(optimResults$par, parSpecs$transformFncs)
    }
    parNames[1:noPars] <- parSpecs$parNames
    nLL <- optimResults$value
    
    summary <- c(expID, expCond, subject, modelName, noPars, pars, parNames, nLL)
    return(summary)
}

# create an empty frame for all the modelig results
modelingResults <- matrix(NA, nrow=0, ncol=26)



# ----
# FINDING PARAMETERS FOR MAB DATA
# ----

registerDoMC(noCores)


print("delta_SM")
estimatedModel <- 
    foreach(s = subjects_MAB, .combine=rbind, .packages="dplyr") %dopar% {
        print(s)
        optimResults <- 
            optfun( objectiveFunction = delta_SM_nLL, 
                    lower = delta_SM_pars$lower, 
                    upper = delta_SM_pars$upper,
                    transformFncs = delta_SM_pars$transformFncs,
                    modelVersion = "delta_SM",
                    data = filter(data_MAB, subjectID==s),
                    noOptimInit = noOptimInit, 
                    noInitPoints = noInitPoints, maxit = maxit)
        getSummary(data = data_MAB,
                   modelName = "delta_SM", 
                   optimResults = optimResults, 
                   subject = s, 
                   parSpecs = delta_SM_pars)
    }
modelingResults <- rbind(modelingResults, estimatedModel)
save.image(file ="interim.RData")


registerDoSEQ()


# ----------------------------------------------------------------------
# Saving results
# ----------------------------------------------------------------------


rownames(modelingResults) <- NULL
modelingResults <- as.data.frame(modelingResults, stringsAsFactors=FALSE)
colnames(modelingResults) <- 
    c("expID", "expCond", "subjectID", "model", "noPars", 
       paste0("par", 1:10), paste0("parNames", 1:10), "nLL")

modelingResults <- convertType(modelingResults,
                                    c(rep("char", 4), 
                                      rep("num",11), 
                                      rep("char",10),
                                      "num") )

save(modelingResults, file = saveFileName)
print("DONE")

