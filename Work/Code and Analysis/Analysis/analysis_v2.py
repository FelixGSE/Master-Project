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

### Source own modules
path_modules = '/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Modules/'
os.chdir(path_modules)  
execfile("Class_Bandit.py")
execfile("Class_Agent.py")
execfile("Class_Data.py")
execfile("Class_Similarity.py")
execfile("Class_Accuracies.py")
execfile("Class_Unsupervised.py")
execfile("Class_Miner.py")

### Source own modules
function_modules = '/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Function/'
os.chdir(path_modules) 
#execfile("Function_Lineplot.py")

# Reset Working Directory
path_data = '/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Artificial Data Sets/'
os.chdir(path_data)  

####################################################################################################

####################################################################################################

#---------------------------------------------------------------------------------------------------
# Bandits
#---------------------------------------------------------------------------------------------------

# Mean of the bandits 
p01 = [0,0.5,1] 
# Standard Deviation of the bandits
p02 = [1,1,1] 	
# Set of number of trials 
p03 = []
# Set of number of clusters	
p04 = 19 		
# Set of seeds
p05 = None

#---------------------------------------------------------------------------------------------------
# Agent
#---------------------------------------------------------------------------------------------------

# Set of decision functions
p06 = "softmax"

# Set of alphas
p07 = [1, 1 , 1] 

# Set of Taus
tau = [0.1,0.5,1]	

#---------------------------------------------------------------------------------------------------
# Analysis 
#---------------------------------------------------------------------------------------------------

prediction_accuracies = miner()
prediction_accuracies.prediction( mu_set = p01, 
								  sigma_set = p02,
								  N_set = p03,
								  cluster_set,
								  seed_set,
								  decision_function_set,
								  alpha_set,
								  tau_set, 
								  epsilon_set = None
								 )

####################################################################################################

####################################################################################################