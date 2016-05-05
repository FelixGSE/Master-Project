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
seed = 10
class_bandit = bandit(mu = means, sigma = sigma ,N=10,seed=seed)
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




class data:

	""" 
    SET INITIAL CONDITIONS
    """

	def __init__(self):
		self.choices = []
		self.rewards = []
		self.value_functions = []



	""" 
    Create data set
    """

    def create_data(self, mu = [0,0], sigma = [1,1], N=10, seed=None,cluster=5, decision_function = "softmax", alpha = [0.1,0.9],tau=[0.1,0.9],epsilon = [0.01,0.1] ):

    	# Create Bandits from module bandit
    	class_bandit = bandit(mu = mu, sigma = sigma ,N=N,seed=seed)
		reward_data = class_bandit.bandits
		nclust = cluster 

		if decision_function == "softmax":

			for i in range( len(alpha) ):
				temp_alpha = alpha[i]
				temp_tau = tau[i]
				for j in range( ncluster ):
					temp_agent = agent( alpha = temp_alpha, tau = temp_tau, reward_input = reward_data,decision_function = decision_function )
					temp_agent.learn()
					self.value_functions.append( temp_agent.value_function )
					self.choices.append( temp_agent.choices )
					self.rewards.append( temp_agent.rewards )

		if decision_function == "epsgreedy":

			for i in range( len(alpha) ):
				temp_alpha = alpha[i]
				temp_epsilon = epsilon[i]
				for j in range( ncluster ):
					temp_agent = agent( alpha = temp_alpha, tau = temp_tau, reward_input = reward_data,decision_function = decision_function )
					temp_agent.learn()
					self.value_functions.append( temp_agent.value_function )
					self.choices.append( temp_agent.choices )
					self.rewards.append( temp_agent.rewards )



####################################################################################################

####################################################################################################