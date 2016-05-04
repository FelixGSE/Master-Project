####################################################################################################

####################################################################################################

### Load packages
import random as rd
import numpy as np
import os 
import json

### Set working directory
os.chdir('/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code/')  

### Source the files
execfile("Class_Bandit.py")
execfile("Class_Agent.py")

####################################################################################################

####################################################################################################

# Create reward data
means = [0,1,2]
sigma = [1,1,1]
class_bandit = bandit(mu = means, sigma = sigma ,N=10)
reward_data = class_bandit.bandits

# Set parameter set
alpha = [0.2,0.5,0.8]
tau = [ 0.1, 0.5, 1, 10]
ncluster = 6

# Storage
choices = []
rewards = []
value_functions = []

# Create data set
for i in range( len(alpha) ):
	temp_alpha = alpha[i]
	temp_tau = tau[i]
	for j in range( ncluster ):
		temp_agent = agent( alpha = temp_alpha, tau = temp_tau, reward_input = reward_data )
		temp_agent.learn()
		value_functions.append( temp_agent.value_function )
		choices.append( temp_agent.choices )
		rewards.append( temp_agent.rewards )

####################################################################################################

####################################################################################################