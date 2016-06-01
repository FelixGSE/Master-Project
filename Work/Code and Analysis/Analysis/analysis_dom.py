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
import csv

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
execfile("Class_Auxilliary.py")
execfile("Class_Data_Clustering.py")

####################################################################################################

####################################################################################################

#---------------------------------------------------------------------------------------------------
# Bandits
#---------------------------------------------------------------------------------------------------

# Mean of the bandits 
p01 = rep([0,2,4],6)
# Standard Deviation of the bandits
p02 = rep([1,1,1],6)
# Set of number of trials 
p03 = rep(100,6)
# Set of size of clusters	
p04 = rep(5,6)



#---------------------------------------------------------------------------------------------------
# Agent
#---------------------------------------------------------------------------------------------------


# Set of decision functions
p06 = rep("softmax",6)

# Set of alphas
p07 = rep([0.5,0.5,0.5], 6 )

# Set of Taus
tau = [ [0.1,0.2,0.3], [0.1,0.3,0.5], [0.1,0.5,0.9],
		[0.3,0.7,1.1], [0.5,0.9,1.3], [0.1,1,5] ] 	


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

print prediction_accuracies.dframe.round(5)

print prediction_accuracies.dframe.round(5).to_csv("../Results/data_5guys_p22_1.csv")
####################################################################################################

####################################################################################################

#Create data
dat = data()

dat.create_data(mu=[0,2,4],sigma=[1,1,1],N=100,cluster_size=10,alpha=[0.5,0.5,0.5],tau=[0.1,1,5])

dat.save_history()

print len(dat.choices)

print pd.DataFrame(dat.choices)

pd.DataFrame(dat.choices).to_csv("../Artificial Data Sets/d02/data_choices.csv")



#########
path_modules = '/home/fizlaz/bgse/Master_Thesis/prisondata_dom/'
os.chdir(path_modules)  
aux = auxilliary()
choices = aux.read_csv('choices_num.csv')
entropy = aux.entropy(choices)

choices_avg = aux.avg(choices)
entropy_avg = aux.avg(entropy)

print choices_avg[0]
print entropy_avg[0]

labels = aux.read_csv2('labels_tab_t.csv',delimiter='\t')

choices2= aux.read_csv('choice_100.csv',delimiter=';')


