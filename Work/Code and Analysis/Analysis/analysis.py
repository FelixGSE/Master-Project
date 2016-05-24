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
#
#---------------------------------------------------------------------------------------------------

# Specify variables  
mu = [0,0.5,1]
sigma = [1,1,1]
cluster = 19
seed = None
decision_function = "softmax"
alpha = [1, 1 , 1]
tau = [0.1,0.5,1]	
N = 100

# Create data set
d01 = data()
d01.create_data( individual = True, mu = mu, sigma = sigma, N = N,cluster_size = cluster, seed = seed, \
				decision_function = decision_function, alpha = alpha,tau = tau)

e01 = d01.entropies
c01 = d01.choices 
l01 = d01.label

# Compute Similiarity
sim = similarity()
sim.timeseries(e01)
sim.categorical(c01)

a01 = sim.edtw
eu01 = sim.euclidian_dist
# Unsupervised
u01 = unsupervised()
u01.fit_all_with_affinity(sim.overlap,3)

# Accuracies
no = len(tau)
pre01 = u01.spectral_prediction
pre02 = u01.affinity_prediction
pre03 = u01.kmeans(c01,no)
pre04 = u01.kmeans(e01,no)
pre05 = u01.kmeans(eu01,no)
pre06 = u01.pca_ward(eu01,2,no)

print "\n"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print "NEW RUN"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print "\n"

acc01 = accuracies(l01,pre01)
acc01.report_accuracies()

acc02 = accuracies(l01,pre02)
acc02.report_accuracies()

acc03 = accuracies(l01,pre03)
acc03.report_accuracies()

acc04 = accuracies(l01,pre05)
acc04.report_accuracies()

acc05 = accuracies(l01,pre06)
acc05.report_accuracies()

#---------------------------------------------------------------------------------------------------
#
#---------------------------------------------------------------------------------------------------
x = range(len(e01[0]))
lineplot(x,e01)




#---------------------------------------------------------------------------------------------------
#
#---------------------------------------------------------------------------------------------------



####################################################################################################

####################################################################################################