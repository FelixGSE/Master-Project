# ----------------------------------------------------------------------
# Information
# ----------------------------------------------------------------------

# This script defines the initial parameters for the modeling of the choices in the training phase and the projective fit in the test phases.


# ----------------------------------------------------------------------
# Defining the initial parameters for all models
# ----------------------------------------------------------------------


# MAB MODELS

delta_SM_pars = 
    list(parNames = c("eta", "theta"),
         lower = c(0, 0),  # eta, theta
         upper  = c(1, 20), 
         transformFncs=list(logit=c(0,1),
                            log=log) )


delta_SMb_pars = 
    list(parNames = c("eta", "theta", "beta"),
         lower = c(0, 0, 0),  # eta, theta, beta
         upper  = c(1, 20, 100), 
         transformFncs=list(logit=c(0,1),
                            log=log,
                            log=log) )


