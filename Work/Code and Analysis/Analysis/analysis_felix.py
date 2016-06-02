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
#path_modules = '/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Modules'
path_modules = '/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Modules/'

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
p01 = rep( [0,0.5,1], 2 )
# Standard Deviation of the bandits
p02 = rep( [1,1,1], 2 )
# Set of number of trials 
p03 = rep( 100 , 2 ) 
# Set of number of clusters	
p04 = rep( 20, 2 ) 		



#---------------------------------------------------------------------------------------------------
# Agent
#---------------------------------------------------------------------------------------------------


# Set of decision functions
p06 = rep("softmax",2)

# Set of alphas
p07 = [ [1,1,1], [1,1,1]
	  ]

# Set of Taus
tau = [ [0.1,0.1,0.1], [0.1,0.2,0.3]
	  ]
	


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
								  epsilon_set = rep(None,6)
								 )
print prediction_accuracies.dframe
prediction_accuracies.dframe.to_csv("../Results/res04.csv")
print prediction_accuracies.dframe.to_latex()
print "\n"


####################################################################################################

####################################################################################################

path_modules = '/Users/felix/Documents/GSE/Term 3/External Data/mixed data/'
os.chdir(path_modules)  
aux = auxilliary()
choices = aux.read_csv('choices_num.csv')
entropy = aux.entropy(choices)
labels = aux.read_csv2('labels_tab_t.csv',delimiter='\t')

choices2= aux.read_csv('choice_100.csv',delimiter=';')[0:161]

unique_labels = list(set(labels))
c00 = aux.subset_data(choices,labels,[1,2,3,4,5,6,7,8,9,10,20])
c01 = aux.subset_data(choices,labels,[1],choices2)
c02 = aux.subset_data(choices,labels,[2],choices2)
c03 = aux.subset_data(choices,labels,[3],choices2)
c04 = aux.subset_data(choices,labels,[4],choices2)
c05 = aux.subset_data(choices,labels,[5],choices2)
c06 = aux.subset_data(choices,labels,[6],choices2)
c07 = aux.subset_data(choices,labels,[7],choices2)
c08 = aux.subset_data(choices,labels,[8],choices2)
c09 = aux.subset_data(choices,labels,[9],choices2)
c10 = aux.subset_data(choices,labels,[10],choices2)
c20 = aux.subset_data(choices,labels,[20],choices2)
c21 = aux.subset_data(choices,labels,[1,2,3,4,5,6,7,8,9,10,20],choices2)

e00 = aux.entropy(c00)
e01 = aux.entropy(c01)
e02 = aux.entropy(c02)
e03 = aux.entropy(c03)
e04 = aux.entropy(c04)
e05 = aux.entropy(c05)
e06 = aux.entropy(c06)
e07 = aux.entropy(c07)
e08 = aux.entropy(c08)
e09 = aux.entropy(c09)
e10 = aux.entropy(c10)
e20 = aux.entropy(c20)
e21 = aux.entropy(c21)

b02 = aux.avg_bad(c02)
# Run computation 00
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/00/')
miner = data_clustering()
miner.prediction(choice_set = c00 , entropy_set = e00 , cluster_range = range(2,10),save = True )
miner.dframe.to_csv("c00_e00.csv")

# Run computation 01
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/01/')
miner = data_clustering()
miner.prediction(choice_set = c01 , entropy_set = e01 , cluster_range = range(2,10),save = True )
miner.dframe.to_csv("c01_e01.csv")

# Run computation 02
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/02/')
miner = data_clustering()
miner.prediction(choice_set = c02 , entropy_set = e02 , bad_set = b02, cluster_range = range(2,10), save = False,path = None )
miner.dframe.to_csv("c02_e02_TEST.csv")

# Run computation 03
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/03/')
miner = data_clustering()
miner.prediction(choice_set = c03 , entropy_set = e03, cluster_range = range(2,10),save = True )
miner.dframe.to_csv("c03_e03.csv")

# Run computation 04
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/04/')
miner = data_clustering()
miner.prediction(choice_set = c04 , entropy_set = e04, cluster_range = range(2,10),save = True )
miner.dframe.to_csv("c04_e04.csv")

# Run computation 05
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/05/')
miner = data_clustering()
miner.prediction(choice_set = c05 , entropy_set = e05, cluster_range = range(2,4),save = True )
miner.dframe.to_csv("c05_e05.csv")

# Run computation 06
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/06/')
miner = data_clustering()
miner.prediction(choice_set = c06 , entropy_set = e06, cluster_range = range(2,10),save = True )
miner.dframe.to_csv("c06_e06.csv")

# Run computation 07
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/07/')
miner = data_clustering()
miner.prediction(choice_set = c07 , entropy_set = e07, cluster_range = range(2,4),save = True )
miner.dframe.to_csv("c07_e07.csv")

# Run computation 08
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/08/')
miner = data_clustering()
miner.prediction(choice_set = c07 , entropy_set = e07, cluster_range = range(2,2),save = True )
miner.dframe.to_csv("c07_e07.csv")

# Run computation 09
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/09/')
miner = data_clustering()
miner.prediction(choice_set = c09 , entropy_set = e09, cluster_range = range(2,7),save = True )
miner.dframe.to_csv("c09_e09.csv")

# Run computation 10
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/10/')
miner = data_clustering()
miner.prediction(choice_set = c10 , entropy_set = e10, cluster_range = range(2,7),save = True )
miner.dframe.to_csv("c09_e09.csv")

# Run computation 20
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/20/')
miner = data_clustering()
miner.prediction(choice_set = c20 , entropy_set = e20, cluster_range = range(2,2),save = True )
miner.dframe.to_csv("c20_e20.csv")

# Run computation 21
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Results/Real data/21/')
miner = data_clustering()
miner.prediction(choice_set = c21 , entropy_set = e21, cluster_range = range(2,10),save = True )
miner.dframe.to_csv("c21_e21.csv")




def jload(self,name):
	with open(name) as file:
		file_content = file.read()
		full_file = json.loads(file_content)
	return full_file


file_handle = open("1929_Hoover_felix.txt") 
file_content = file_handle.read()
speech = json.loads(file_content)



