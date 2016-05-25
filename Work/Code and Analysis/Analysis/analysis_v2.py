####################################################################################################

####################################################################################################

### Load Modules
import random as rd
import numpy as np
import os 
import json
import time
import math 
import sklearn.metrics as met
import sklearn.metrics.cluster as mclu
import sklearn.metrics.pairwise as pa
import sklearn.cluster as clu
import dtw 
import sklearn.decomposition as decomp
import pandas as pd

### Source own modules
path_modules = '/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Modules'
#path_modules = '/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Modules/'

os.chdir(path_modules)  
execfile("Class_Bandit.py")
execfile("Class_Agent.py")
execfile("Class_Data.py")
execfile("Class_Similarity.py")
execfile("Class_Accuracies.py")
execfile("Class_Unsupervised.py")
execfile("Class_Miner.py")
execfile("Function_Auxilliary.py")

####################################################################################################

####################################################################################################

#---------------------------------------------------------------------------------------------------
# Bandits
#---------------------------------------------------------------------------------------------------

# Mean of the bandits 
p01 = [ [0,0.5,1], [0,1,2] ]
# Standard Deviation of the bandits
p02 = [ [1,1,1], [1,1,1] ] 
# Set of number of trials 
p03 = [100,100]
# Set of number of clusters	
p04 = [20,20] 		



#---------------------------------------------------------------------------------------------------
# Agent
#---------------------------------------------------------------------------------------------------


# Set of decision functions
p06 = rep("softmax",2)

# Set of alphas
p07 = [ [1,2,3], [1,2,3] ]

# Set of Taus
tau = [ [0.1,0.5,0.8], [0.1,1,2] ] 	


#---------------------------------------------------------------------------------------------------
# Analysis 
#---------------------------------------------------------------------------------------------------

prediction_accuracies = miner()
prediction_accuracies.prediction( mu_set = p01, 
								  sigma_set = p02,
								  N_set = p03,
								  cluster_set = p04,
								  seed_set = None,
								  decision_function_set = p06,
								  alpha_set = p07,
								  tau_set = tau, 
								  epsilon_set = None
								 )

print prediction_accuracies.dframe.round(5).to_csv("dataaaaaa.csv")
####################################################################################################

####################################################################################################