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

class miner:

	def __init__(self):

		self.accuracy_set = []


	def prediction(self, mu_set, sigma_set,N_set,cluster_set,seed_set,decision_function_set,alpha_set,tau_set,epsilon_set = None):

		runtime = range(len(mu_set))

		for step in runtime:

			# Print trace
			print "\n"
			print "*************************************"
			print "Started with iteration \t " + str(step)
			print "-------------------------------------"

			# Subset data 
			mu = mu_set[step]
			sigma = sigma_set[step]
			N = N_set[step]
			cluster = cluster_set[step]
			seed = None
			decision_function = decision_function_set[step]
			alpha = alpha_set[step]
			tau = tau_set[step]
			if epsilon_set == None:
				epsilon = None
			else:
				epsilon = epsilon_set[step]

			# Create data 
			temp_data = data()
			temp_data.create_data( individual = True, mu = mu, sigma = sigma, N = N,
							cluster_size = cluster, seed = seed, decision_function = decision_function, 
							alpha = alpha, tau = tau )
			
			# Extract features
			temp_entropy = temp_data.entropies
			temp_choices = temp_data.choices 
			temp_labels  = temp_data.label

			# Compute Similarities
			sim = similarity()
			sim.timeseries(temp_entropy)
			sim.categorical(temp_choices)
			temp_timewarp = sim.edtw
			temp_eucliddist = sim.euclidian_dist
			temp_overlap = sim.overlap
			
			# Compute Predictions
			no_clust = len(alpha)
			temp_unsupervised = unsupervised()

			p01 = temp_unsupervised.spectral( temp_timewarp, no_clust)
			p02 = temp_unsupervised.affinity_propagation( temp_timewarp )
			p03 = temp_unsupervised.pca_ward(temp_eucliddist,2,no_clust)
			p04 = temp_unsupervised.kmeans(temp_choices,no_clust)
			p05 = temp_unsupervised.spectral( temp_overlap, no_clust)
			p_set = [p01,p02,p03,p04,p05]

			# Compute accuracies
			acc_vector = self.full_accuracies(temp_labels,p_set)
			self.accuracy_set.append(acc_vector)


			print "Finished with iteration  " + str(step)
			print "*************************************"
			print "\n .\n . \n . \n"

	def full_accuracies(self,true,prediction_set):
		all_accurracies = []
		for prediction in prediction_set:
			temp_accuracies = accuracies(true,prediction)
			all_accurracies.append( temp_accuracies.full )
		return all_accurracies


test = miner()

s01 = [[0,0.5,1],[1,2,3]]
s02 = [[1,1,1],[1,1,1]]
s03 = [5,5]
s04 = [None,None]
s05 = ["softmax","softmax"]
s06 = [[1, 1 ],[1, 1 ]]
s07 = [[0.1,1],[0.1,2]	]
s08 = [100,10]
test.prediction(mu_set = s01,sigma_set = s02,N_set = s08 ,cluster_set = s03,seed_set = None ,decision_function_set = s05,alpha_set = s06,tau_set = s07)




####################################################################################################

####################################################################################################