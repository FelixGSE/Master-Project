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
p03 = rep(10,6)
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
choice_bad = aux.avg_bad(choices)

print choices_avg[0]
print entropy_avg[0]
print choice_bad[1]
print choices[0]

labels = aux.read_csv2('labels_tab_t.csv',delimiter='\t')

choices2= aux.read_csv('choice_100.csv',delimiter=';')[:162]

choices2 = pd.read_csv('choice_100.csv')[:162]
choices2 = choices2.values.tolist()

print choices2
print choices2.shape

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

l00 = aux.labels(labels,[1,2,3,4,5,6,7,8,9,10,20])
l01 = aux.labels(labels,[1],n=None)
l02 = aux.labels(labels,[2],n=None)
l03 = aux.labels(labels,[3],n=None)
l04 = aux.labels(labels,[4],n=None)
l05 = aux.labels(labels,[5],n=None)
l06 = aux.labels(labels,[6],n=None)
l07 = aux.labels(labels,[7],n=None)
l08 = aux.labels(labels,[8],n=None)
l09 = aux.labels(labels,[9],n=None)
l10 = aux.labels(labels,[10],n=None)
l20 = aux.labels(labels,[20],n=None)
l21 = aux.labels(labels,[1,2,3,4,5,6,7,8,9,10,20],n=None)




# Run computation 01
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/')
miner = data_clustering()
miner.prediction(choice_set = c01 , entropy_set = e01 , labelset=l01, cluster_range = range(2,10),save = False )
miner.dframe.to_csv("c01_e01_dom.csv")



print len(c01[0])

c01 = [[1,2,3,4],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
e01 = aux.entropy(c01)
l01 = [1,2,1,1]

print l01