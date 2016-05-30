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




#### ranking per metric
df = prediction_accuracies.dframe.round(5)
print df["norm mis"]
print len(df["norm mis"])
print df.ix[:,0]

for i in range(len(df["norm mis"])/22):
	print ([df["norm mis"][i*22:(i+1)*22],\
	df["norm mis"][i*22:(i+1)*22].rank(method="min")])


print df.columns.values[10:]

for i in range(10,17):
	print df.columns.values[i]

print df["norm mis"][:22]

print df["norm mis"][:22].rank(method="min")

ser = df["norm mis"][:22].rank(method="min")
print ser.round(0)


for i in df["norm mis"][:22].rank(method="min"):
	print int(i)

print np.array(df["norm mis"][:22])

print np.vstack((np.array(df["norm mis"][:22]),np.array(df["norm mis"][:22].rank(method="min"))))

print zip(df["norm mis"][:22],df["norm mis"][:22].rank(method="min"))

zipped = zip(df["norm mis"][:22],df["norm mis"][:22].rank(method="min"))
print type(zipped)


for i in zipped:
	print list(i)


for i in df.columns.values[10:]:
	print type(i)


for step in range(6):
	p_len = 22
	for i in df.columns.values[10:]:
		#print zip(df[i][step*p_len:(step+1)*p_len],df[i][step*p_len:(step+1)*p_len].rank(method="min"))
		df[i][step*p_len:(step+1)*p_len].replace(zip(df[i][step*p_len:(step+1)*p_len],df[i][step*p_len:(step+1)*p_len].rank(method="min")))
		print df[i][step*p_len:(step+1)*p_len]
		#df[i][step*p_len:(step+1)*p_len]=df[i][step*p_len:(step+1)*p_len]**2


print np.NAN

dom = [np.NAN,np.NAN]
print dom

print df.ix[1,16]

print df.dtypes

l=[[1,2,1],[3]]
print sum(l, [])


