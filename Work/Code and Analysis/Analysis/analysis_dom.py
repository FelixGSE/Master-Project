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
#execfile("Function_Auxilliary.py")
execfile("Class_Auxilliary.py")
execfile("Class_Data_Clustering.py")

####################################################################################################

####################################################################################################

#---------------------------------------------------------------------------------------------------
# Bandits
#---------------------------------------------------------------------------------------------------

# Mean of the bandits 
p01 = rep([0,0.5,1],1)
# Standard Deviation of the bandits
p02 = rep([1,1,1],1)
# Set of number of trials 
p03 = rep(100,1)
# Set of size of clusters	
p04 = rep(5,1)



#---------------------------------------------------------------------------------------------------
# Agent
#---------------------------------------------------------------------------------------------------


# Set of decision functions
p06 = rep("softmax",1)

# Set of alphas
p07 = rep([0.5,0.5,0.5], 1 )

# Set of Taus
tau = [ [0.1,0.2,0.3], [0.1,0.3,0.5], [0.1,0.5,0.9],
		[0.3,0.7,1.1], [0.5,0.9,1.3], [0.1,1,5] ] 	

tau = [ [0.1,0.7,1.8] ]


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
								  epsilon_set = None,
								  iowa = True
								 )

print prediction_accuracies.dframe.round(5)

print prediction_accuracies.dframe.round(5).to_csv("../Results/Simulation/data_20guys_p22_IOWA.csv")

####################################################################################################

####################################################################################################

#Create data
dat = data()

dat.create_data(mu=[0,0.5,1],sigma=[1,1,1],N=100,cluster_size=20,alpha=[0.5,0.5,0.5],tau=[0.1,0.7,1.8],iowa=True)

dat.save_history('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Data/Artificial Data Sets/d06/')

print len(dat.choices)

print pd.DataFrame(dat.choices)

pd.DataFrame(dat.choices).to_csv("../Artificial Data Sets/d02/data_choices.csv")

#####
cho = pd.read_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Data/Artificial Data Sets/d06/choices_softmax_00_29_58.txt', sep=",", header = None)
cho = choices2.values.tolist()

#####
choc = aux.jload('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Data/Artificial Data Sets/d06/choices_softmax_00_29_58.txt')
ebsim = aux.entropy_block(choc)

pd.DataFrame(ebsim).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Data/Artificial Data Sets/d06/ebsim.csv')

#####


#########
path_modules = '/home/fizlaz/bgse/Master_Thesis/prisondata_dom/'
os.chdir(path_modules)  
aux = auxilliary()
choices = aux.read_csv('choices_num.csv')
entropy = aux.entropy(choices)
entropy_block = aux.entropy_block(choices)

choices_avg = aux.avg(choices)
entropy_avg = aux.avg(entropy)
choice_bad = aux.avg_bad(choices)


#labels = aux.read_csv2('labels_tab_t.csv',delimiter='\t')

#choices2= aux.read_csv('choice_100.csv',delimiter=';')[:162]
index_normal = pd.read_csv("index_100.csv")
#print index_normal[index_normal[,1]=="Wood"]

choices2 = pd.read_csv('choice_100.csv')[:162]
choices2 = choices2.values.tolist()

#print choices2

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
e66 = aux.entropy(choices2)

eb00 = aux.entropy_block(c00)
eb01 = aux.entropy_block(c01)
eb02 = aux.entropy_block(c02)
eb03 = aux.entropy_block(c03)
eb04 = aux.entropy_block(c04)
eb05 = aux.entropy_block(c05)
eb06 = aux.entropy_block(c06)
eb07 = aux.entropy_block(c07)
eb08 = aux.entropy_block(c08)
eb09 = aux.entropy_block(c09)
eb10 = aux.entropy_block(c10)
eb20 = aux.entropy_block(c20)
eb21 = aux.entropy_block(c21)
eb66 = aux.entropy_block(choices2)

l00 = aux.labels(labels,[1,2,3,4,5,6,7,8,9,10,20],healthy=False)
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

b00 = aux.avg_bad(c00)
b01 = aux.avg_bad(c01)
b02 = aux.avg_bad(c02)
b03 = aux.avg_bad(c03)
b04 = aux.avg_bad(c04)
b05 = aux.avg_bad(c05)
b06 = aux.avg_bad(c06)
b07 = aux.avg_bad(c07)
b08 = aux.avg_bad(c08)
b09 = aux.avg_bad(c09)
b10 = aux.avg_bad(c10)
b20 = aux.avg_bad(c20)
b21 = aux.avg_bad(c21)





pd.DataFrame(c00).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/00/c00.csv')
pd.DataFrame(c01).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/c01.csv')
pd.DataFrame(c02).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/c02.csv')
pd.DataFrame(c03).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/c03.csv')
pd.DataFrame(c04).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/c04.csv')
pd.DataFrame(c05).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/05/c05.csv')
pd.DataFrame(c06).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/c06.csv')
pd.DataFrame(c07).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/07/c07.csv')
pd.DataFrame(c08).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/08/c08.csv')
pd.DataFrame(c09).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/c09.csv')
pd.DataFrame(c10).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/10/c10.csv')
pd.DataFrame(c20).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/20/c20.csv')
pd.DataFrame(c21).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/21/c21.csv')
pd.DataFrame(choices2).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/66/c66.csv')


pd.DataFrame(b00).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/00/b00.csv')
pd.DataFrame(b01).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/b01.csv')
pd.DataFrame(b02).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/b02.csv')
pd.DataFrame(b03).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/b03.csv')
pd.DataFrame(b04).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/b04.csv')
pd.DataFrame(b05).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/05/b05.csv')
pd.DataFrame(b06).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/b06.csv')
pd.DataFrame(b07).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/07/b07.csv')
pd.DataFrame(b08).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/08/b08.csv')
pd.DataFrame(b09).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/b09.csv')
pd.DataFrame(b10).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/10/b10.csv')
pd.DataFrame(b20).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/20/b20.csv')
pd.DataFrame(b21).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/21/b21.csv')


pd.DataFrame(e00).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/00/e00.csv')
pd.DataFrame(e01).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/e01.csv')
pd.DataFrame(e02).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/e02.csv')
pd.DataFrame(e03).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/e03.csv')
pd.DataFrame(e04).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/e04.csv')
pd.DataFrame(e05).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/05/e05.csv')
pd.DataFrame(e06).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/e06.csv')
pd.DataFrame(e07).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/07/e07.csv')
pd.DataFrame(e08).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/08/e08.csv')
pd.DataFrame(e09).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/e09.csv')
pd.DataFrame(e10).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/10/e10.csv')
pd.DataFrame(e20).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/20/e20.csv')
pd.DataFrame(e21).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/21/e21.csv')
pd.DataFrame(e66).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/66/e66.csv')


pd.DataFrame(eb00).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/00/eb00.csv')
pd.DataFrame(eb01).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/eb01.csv')
pd.DataFrame(eb02).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/eb02.csv')
pd.DataFrame(eb03).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/eb03.csv')
pd.DataFrame(eb04).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/eb04.csv')
pd.DataFrame(eb05).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/05/eb05.csv')
pd.DataFrame(eb06).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/eb06.csv')
pd.DataFrame(eb07).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/07/eb07.csv')
pd.DataFrame(eb08).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/08/eb08.csv')
pd.DataFrame(eb09).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/eb09.csv')
pd.DataFrame(eb10).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/10/eb10.csv')
pd.DataFrame(eb20).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/20/eb20.csv')
pd.DataFrame(eb21).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/21/eb21.csv')
pd.DataFrame(eb66).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/66/eb66.csv')


# Run computation 00
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/00/')
miner = data_clustering()
miner.prediction(choice_set = c00 , entropy_set = e00 , cluster_range = range(2,10),labelset=l00,save = False )
miner.dframe.to_csv("c00_e00_dom.csv")

# Run computation 01
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/')
miner = data_clustering()
miner.prediction(choice_set = c01 , entropy_set = e01 , cluster_range = range(2,10),labelset=l01,save = False )
miner.dframe.to_csv("c01_e01_dom.csv")

# Run computation 02
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/')
miner = data_clustering()
miner.prediction(choice_set = c02 , entropy_set = e02 , bad_set = b02,labelset = l02,ent_block=eb02, cluster_range = range(2,4), save = False)
miner.dframe.to_csv("c02_e02_dom_eb.csv")

# Run computation 06
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/')
miner = data_clustering()
miner.prediction(choice_set = c06 , entropy_set = e06 , bad_set = b06,labelset = l06,ent_block=eb06, cluster_range = range(2,10), save = False)
miner.dframe.to_csv("c06_e06_dom_eb.csv")


########################################################################
#hrvoje multiarm data

#########
path_modules = '/home/fizlaz/bgse/Master_Thesis/hrvoje_multiarm/'
os.chdir(path_modules)  

hrv_choices = pd.read_csv("hrvoje_multiarm_choices.csv")
hrv_choices = hrv_choices.values.tolist()

hrv_gender = pd.read_csv("hrvoje_multiarm_gender.csv")
hrv_gender = hrv_gender['x'].values.tolist()

label = [0] * 104
for i in range(104):
	if hrv_gender[i]=="Male":
		label[i]=1


aux = auxilliary()

entropy = aux.entropy(hrv_choices)
entropy_block = aux.entropy_block(hrv_choices)

choices_avg = aux.avg(hrv_choices)
entropy_avg = aux.avg(entropy)
choice_bad = aux.avg_bad(hrv_choices)



c00 = aux.subset_data(hrv_choices,label,[0,1])


e00 = aux.entropy(c00)


eb00 = aux.entropy_block(c00)


l00 = aux.labels(label,[0,1],healthy=False)

b00 = aux.avg_bad(c00)



# Run computation 06
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real_data_multiarm/')
miner = data_clustering()
miner.prediction(choice_set = c00 , entropy_set = e00 , bad_set = c00,labelset = l00,ent_block=eb00, cluster_range = range(2,3), save = True)
miner.dframe.to_csv("c01_dom.csv")



import matplotlib.pyplot as plt
plt.plot(c00[100]),plt.show()
