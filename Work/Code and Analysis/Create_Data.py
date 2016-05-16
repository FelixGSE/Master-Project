####################################################################################################

####################################################################################################

### Load Modules
import random as rd
import numpy as np
import os 
import json
import time
import math 

### Source own modules
path_modules = '/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Modules/'
os.chdir(path_modules)  
execfile("Class_Bandit.py")
execfile("Class_Agent.py")
execfile("Class_Data.py")


# Reset Working Directory
path_data = '/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Artificial Data Sets/'
os.chdir(path_data)  

####################################################################################################

####################################################################################################

# Specify variables  
mu = [1,2,3]
sigma = [1,1,1]
cluster = 4
seed = None
decision_function = "softmax"
epsilon = [0,0] 
alpha = [0.5, 1 , 0.5 ]
tau = [0.1,0.5,10]	
N = 100

# Create data set

d01 = data()
d01.create_data( individual = True, mu = mu, sigma = sigma, N = N,cluster_size = cluster, seed = seed, \
				decision_function = decision_function, alpha = alpha,tau = tau,epsilon=epsilon)

sim = similarity()
y =d01.entropies
y2 = d01.choices 
sim.timeseries(y)
sim.categorical(y2)

aff = sim.edtw
aff2 = sim.overlap
print 
import sklearn.cluster as clu
spec = clu.SpectralClustering(n_clusters=3,affinity = 'precomputed')
spec.fit_predict(aff)
p = spec.labels_
t = d01.label


acc = accuracies(t,p)
acc.report_accuracies()
print p
print t


y =d01.choices
x = range(N)
y =d01.entropies
lineplot(x,[y[2]])
# Save data set to HD
path_set = "d01"
os.mkdir( path_set )
path = path_data + path_set + "/"
d01.save_history( path = path )


####################################################################################################

####################################################################################################