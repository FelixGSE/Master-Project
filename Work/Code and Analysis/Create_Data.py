####################################################################################################

####################################################################################################

### Load Modules
import random as rd
import numpy as np
import os 
import json
import time

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
mu = [0,0]
sigma = [1,1]
cluster = 10
seed = 123
cluster = 10
decision_function = "softmax" 
alpha = [ 0.5 , 0.5 ]
	
        
# Create data set
d01 = data()
d01.create_data( mu = mu, sigma = sigma, cluster = cluster, seed = seed, \
				decision_function = decision_function, alpha = alpha, tau = tau )

# Save data set to HD
path_set = "d01"
os.mkdir( path_set )
path = path_data + path_set + "/"
d01.save_history( path = path )


####################################################################################################

####################################################################################################