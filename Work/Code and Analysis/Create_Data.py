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
mu = [0,2]
sigma = [1,1]
cluster = 10
seed = 123
decision_function = "epsgreedy"
epsilon = [0,0] 
alpha = [ 1 , 1 ]
tau = [0.1,0.1]	
N = 3000

# Create data set

d01 = data()
d01.create_data( mu = mu, sigma = sigma, N = N,cluster_size = cluster, seed = seed, \
				decision_function = decision_function, alpha = alpha,tau = tau,epsilon=epsilon)


y =d01.choices
x = range(N)
y =d01.entropies
lineplot(x,y)
# Save data set to HD
path_set = "d01"
os.mkdir( path_set )
path = path_data + path_set + "/"
d01.save_history( path = path )


####################################################################################################

####################################################################################################