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
import editdistance

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
execfile("Class_Data_Clustering_Looping.py")

####################################################################################################

####################################################################################################

aux=auxilliary()

#---------------------------------------------------------------------------------------------------
# Bandits
#---------------------------------------------------------------------------------------------------

# Mean of the bandits 
p01 = aux.rep([0,2,4],6)
# Standard Deviation of the bandits
p02 = aux.rep([1,1,1],6)
# Set of number of trials 
p03 = aux.rep(100,6)
# Set of size of clusters	
p04 = aux.rep(10,6)



#---------------------------------------------------------------------------------------------------
# Agent
#---------------------------------------------------------------------------------------------------


# Set of decision functions
p06 = aux.rep("softmax",6)

# Set of alphas
p07 = aux.rep([1,1], 6 )

# Set of Taus
tau = [ [0.1,0.3], [0.1,0.5], [0.1,0.7],
		[0.1,1], [0.1,1.5], [0.1,2] ] 	

#tau = [ [0.1,0.7,1.8] ]
tau=aux.rep([1.5,1.5],6)

p07 = [[0.1,0.3], [0.1,0.5], [0.1,0.7],
	   [0.1,0.9], [0.5,0.9], [0.7,0.9]]


p07 = [[0.1,1], [0.05,1], [0.01,1],
	   [0.001,1], [0.0001,1], [0.00001,1]]


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
								  iowa = False
								 )

print prediction_accuracies.dframe.round(5)

print prediction_accuracies.dframe.round(5).to_csv("../Results/Simulation_new_2/data_mean2_a_xtrm_t_15_1.csv")

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


labels = aux.read_csv2('labels_tab_t.csv',delimiter='\t')

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

#####################################################
##################################################### all above are mixed with healthy
c01 = aux.subset_data(choices,labels,[1])
c02 = aux.subset_data(choices,labels,[2])
c03 = aux.subset_data(choices,labels,[3])
c04 = aux.subset_data(choices,labels,[4])
c06 = aux.subset_data(choices,labels,[6])
c09 = aux.subset_data(choices,labels,[9])

e01 = aux.entropy(c01)
e02 = aux.entropy(c02)
e03 = aux.entropy(c03)
e04 = aux.entropy(c04)
e06 = aux.entropy(c06)
e09 = aux.entropy(c09)

eb01 = aux.entropy_block(c01)
eb02 = aux.entropy_block(c02)
eb03 = aux.entropy_block(c03)
eb04 = aux.entropy_block(c04)
eb06 = aux.entropy_block(c06)
eb09 = aux.entropy_block(c09)

b01 = aux.avg_bad(c01)
b02 = aux.avg_bad(c02)
b03 = aux.avg_bad(c03)
b04 = aux.avg_bad(c04)
b06 = aux.avg_bad(c06)
b09 = aux.avg_bad(c09)


bc1 = aux.avg_bad_cum(c01)
bc2 = aux.avg_bad_cum(c02)
bc3 = aux.avg_bad_cum(c03)
bc4 = aux.avg_bad_cum(c04)
bc6 = aux.avg_bad_cum(c06)
bc9 = aux.avg_bad_cum(c09)







pd.DataFrame(c00).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/00/c00_SOLO.csv')
pd.DataFrame(c01).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/c01_SOLO.csv')
pd.DataFrame(c02).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/c02_SOLO.csv')
pd.DataFrame(c03).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/c03_SOLO.csv')
pd.DataFrame(c04).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/c04_SOLO.csv')
pd.DataFrame(c05).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/05/c05_SOLO.csv')
pd.DataFrame(c06).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/c06_SOLO.csv')
pd.DataFrame(c07).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/07/c07_SOLO.csv')
pd.DataFrame(c08).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/08/c08_SOLO.csv')
pd.DataFrame(c09).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/c09_SOLO.csv')
pd.DataFrame(c10).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/10/c10_SOLO.csv')
pd.DataFrame(c20).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/20/c20_SOLO.csv')
pd.DataFrame(c21).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/21/c21_SOLO.csv')
pd.DataFrame(choices2).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/66/c66.csv')


pd.DataFrame(b00).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/00/b00_SOLO.csv')
pd.DataFrame(b01).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/b01_SOLO.csv')
pd.DataFrame(b02).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/b02_SOLO.csv')
pd.DataFrame(b03).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/b03_SOLO.csv')
pd.DataFrame(b04).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/b04_SOLO.csv')
pd.DataFrame(b05).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/05/b05_SOLO.csv')
pd.DataFrame(b06).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/b06_SOLO.csv')
pd.DataFrame(b07).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/07/b07_SOLO.csv')
pd.DataFrame(b08).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/08/b08_SOLO.csv')
pd.DataFrame(b09).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/b09_SOLO.csv')
pd.DataFrame(b10).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/10/b10_SOLO.csv')
pd.DataFrame(b20).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/20/b20_SOLO.csv')
pd.DataFrame(b21).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/21/b21_SOLO.csv')


pd.DataFrame(e00).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/00/e00_SOLO.csv')
pd.DataFrame(e01).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/e01_SOLO.csv')
pd.DataFrame(e02).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/e02_SOLO.csv')
pd.DataFrame(e03).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/e03_SOLO.csv')
pd.DataFrame(e04).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/e04_SOLO.csv')
pd.DataFrame(e05).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/05/e05_SOLO.csv')
pd.DataFrame(e06).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/e06_SOLO.csv')
pd.DataFrame(e07).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/07/e07_SOLO.csv')
pd.DataFrame(e08).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/08/e08_SOLO.csv')
pd.DataFrame(e09).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/e09_SOLO.csv')
pd.DataFrame(e10).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/10/e10_SOLO.csv')
pd.DataFrame(e20).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/20/e20_SOLO.csv')
pd.DataFrame(e21).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/21/e21_SOLO.csv')
pd.DataFrame(e66).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/66/e66_SOLO.csv')


pd.DataFrame(eb00).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/00/eb00_SOLO.csv')
pd.DataFrame(eb01).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/eb01_SOLO.csv')
pd.DataFrame(eb02).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/eb02_SOLO.csv')
pd.DataFrame(eb03).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/eb03_SOLO.csv')
pd.DataFrame(eb04).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/eb04_SOLO.csv')
pd.DataFrame(eb05).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/05/eb05_SOLO.csv')
pd.DataFrame(eb06).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/eb06_SOLO.csv')
pd.DataFrame(eb07).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/07/eb07_SOLO.csv')
pd.DataFrame(eb08).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/08/eb08_SOLO.csv')
pd.DataFrame(eb09).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/eb09_SOLO.csv')
pd.DataFrame(eb10).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/10/eb10_SOLO.csv')
pd.DataFrame(eb20).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/20/eb20_SOLO.csv')
pd.DataFrame(eb21).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/21/eb21_SOLO.csv')
pd.DataFrame(eb66).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/66/eb66_SOLO.csv')


pd.DataFrame(bc1).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/bc1_SOLO.csv')
pd.DataFrame(bc2).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/bc2_SOLO.csv')
pd.DataFrame(bc3).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/bc3_SOLO.csv')
pd.DataFrame(bc4).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/bc4_SOLO.csv')
pd.DataFrame(bc6).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/bc6_SOLO.csv')
pd.DataFrame(bc9).to_csv('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/bc9_SOLO.csv')


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

# Run computation 01 new
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/01/')
miner = data_clustering()
miner.prediction(choice_set = c01 , entropy_set = e01 , bad_set = b01,labelset = l01,ent_block=eb01, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c01_e01_dom_b_cum_rerun1.csv")

# Run computation 02
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02/')
miner = data_clustering()
miner.prediction(choice_set = c02 , entropy_set = e02 , bad_set = b02,labelset = l02,ent_block=eb02, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c02_e02_dom_b_cum_rerun1.csv")

# Run computation 03
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/03/')
miner = data_clustering()
miner.prediction(choice_set = c03 , entropy_set = e03 , bad_set = b03,labelset = l03,ent_block=eb03, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c03_e03_dom_b_cum_rerun1.csv")

# Run computation 04
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/04/')
miner = data_clustering()
miner.prediction(choice_set = c04 , entropy_set = e04 , bad_set = b04,labelset = l04,ent_block=eb04, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c04_e04_dom_b_cum_rerun1.csv")

# Run computation 06
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06/')
miner = data_clustering()
miner.prediction(choice_set = c06 , entropy_set = e06 , bad_set = b06,labelset = l06,ent_block=eb06, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c06_e06_dom_b_cum_rerun3.csv")

# Run computation 09
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/09/')
miner = data_clustering()
miner.prediction(choice_set = c09 , entropy_set = e09 , bad_set = b09,labelset = l09,ent_block=eb09, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c09_e09_dom_b_cum_rerun1.csv")



########################################################################
#hrvoje multiarm data

#########
path_modules = '/home/fizlaz/bgse/Master_Thesis/hrvoje_multiarm/'
os.chdir(path_modules)

hrv_exptype =  pd.read_csv("hrvoje_multiarm_exptype.csv")

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

label = range(390,429)


#c00 = aux.subset_data(hrv_choices,label,[0,1])

c00 = hrv_choices[390:429]

e00 = aux.entropy(c00)


eb00 = aux.entropy_block(c00)

l00 = label

#l00 = aux.labels(label,[0,1],healthy=False)

b00 = aux.avg_bad(c00)



# Run computation 06
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real_data_multiarm/exp1_2/')
miner = data_clustering()
miner.prediction(choice_set = c00 , entropy_set = e00 , bad_set = e00,labelset = l00,ent_block=eb00, cluster_range = range(2,4), save = True)
miner.dframe.to_csv("c00_exp4_1.csv")


print miner.dframe[["algorithm","predictions"]]

miner.dframe[["algorithm","predictions"]].to_json("JSON_exp4_1.txt")



print miner.dframe.iloc[0:68, 1:3]


a = pd.read_json("JSON_exp4_1.txt")
print a.iloc[0:68,:]

print a.sort_index().iloc[:68,:]
a.sort_index().iloc[0:68,:].to_json("JSON_exp4_1_CL2.txt")

print a.sort_index().iloc[68:,:]
a.sort_index().iloc[68:,:].to_json("JSON_exp4_1_CL3.txt")

#####################
b = pd.read_json("JSON_exp2_1.txt")

print b.sort_index().iloc[:68,:]
b.sort_index().iloc[:68,:].to_json("JSON_exp2_1_CL2.txt")

print b.sort_index().iloc[68:,:]
b.sort_index().iloc[68:,:].to_json("JSON_exp2_1_CL3.txt")

#################
c = pd.read_json("FELIX_JSON_2_3_CLUSTERS.txt")

print c.sort_index().iloc[68:,:]
c.sort_index().iloc[68:,:].to_json("JSON_exp1_2_CL3.txt")


import matplotlib.pyplot as plt
plt.plot(c00[100]),plt.show()


############## yechiam data

os.chdir('/home/fizlaz/bgse/Master_Thesis/')  

ch_drug_1 = pd.read_csv("yechiam_drugs_pd_choices_v1.csv")
ch_drug_1 = ch_drug_1.values.tolist()

ch_drug_2 = pd.read_csv("yechiam_drugs_pd_choices_v2.csv")
ch_drug_2 = ch_drug_2.values.tolist()

ch_normal_1 = pd.read_csv("yechiam_normals_pd_choices_v1.csv")
ch_normal_1 = ch_normal_1.values.tolist()

ch_normal_2 = pd.read_csv("yechiam_normals_pd_choices_v2.csv")
ch_normal_2 = ch_normal_2.values.tolist()


e_d1 = aux.entropy(ch_drug_1)
e_d2 = aux.entropy(ch_drug_2)
e_n1 = aux.entropy(ch_normal_1)
e_n2 = aux.entropy(ch_normal_2)

eb_d1 = aux.entropy_block(ch_drug_1)
eb_d2 = aux.entropy_block(ch_drug_2)
eb_n1 = aux.entropy_block(ch_normal_1)
eb_n2 = aux.entropy_block(ch_normal_2)


b_d1 = aux.avg_bad(ch_drug_1)
b_d2 = aux.avg_bad(ch_drug_2)
b_n1 = aux.avg_bad(ch_normal_1)
b_n2 = aux.avg_bad(ch_normal_2)


pd.DataFrame(e_d1).to_csv('/home/fizlaz/bgse/Master_Thesis/e_d1.csv')
pd.DataFrame(e_d2).to_csv('/home/fizlaz/bgse/Master_Thesis/e_d2.csv')
pd.DataFrame(e_n1).to_csv('/home/fizlaz/bgse/Master_Thesis/e_n1.csv')
pd.DataFrame(e_n2).to_csv('/home/fizlaz/bgse/Master_Thesis/e_n2.csv')

pd.DataFrame(eb_d1).to_csv('/home/fizlaz/bgse/Master_Thesis/eb_d1.csv')
pd.DataFrame(eb_d2).to_csv('/home/fizlaz/bgse/Master_Thesis/eb_d2.csv')
pd.DataFrame(eb_n1).to_csv('/home/fizlaz/bgse/Master_Thesis/eb_n1.csv')
pd.DataFrame(eb_n2).to_csv('/home/fizlaz/bgse/Master_Thesis/eb_n2.csv')

pd.DataFrame(b_d1).to_csv('/home/fizlaz/bgse/Master_Thesis/b_d1.csv')
pd.DataFrame(b_d2).to_csv('/home/fizlaz/bgse/Master_Thesis/b_d2.csv')
pd.DataFrame(b_n1).to_csv('/home/fizlaz/bgse/Master_Thesis/b_n1.csv')
pd.DataFrame(b_n2).to_csv('/home/fizlaz/bgse/Master_Thesis/b_n2.csv')


############################################ cocaine

os.chdir('/home/fizlaz/bgse/Master_Thesis/hrvoje_new/s_Stout_etal_2004_cocaine/')  

files=[]
for i in range(2,33):
  if i < 10:
	files.append('g0'+str(i)+'.txt')
  else:
	files.append('g'+str(i)+'.txt')

cocaine_data = []
for sub in files:
  temp = pd.read_csv(sub, sep="\t", header = None).ix[:,0].tolist()
  cocaine_data.append(temp)

remove = [2,11,16,24,30]

coc_data =[element for i,element in enumerate(cocaine_data) if cocaine_data.index(element)  not in remove ]

ent = aux.entropy(coc_data)
ent_b = aux.entropy_block(coc_data)
bad = aux.avg_bad(coc_data)

control = coc_data[:14]
cocaine = coc_data[14:]

e_c = aux.entropy(control)
e_d = aux.entropy(cocaine)

eb_c = aux.entropy_block(control)
eb_d = aux.entropy_block(cocaine)

b_c = aux.avg_bad(control)
b_d = aux.avg_bad(cocaine)


pd.DataFrame(e_c).to_csv('/home/fizlaz/bgse/Master_Thesis/e_c.csv')
pd.DataFrame(e_d).to_csv('/home/fizlaz/bgse/Master_Thesis/e_d.csv')
pd.DataFrame(eb_c).to_csv('/home/fizlaz/bgse/Master_Thesis/eb_c.csv')
pd.DataFrame(eb_d).to_csv('/home/fizlaz/bgse/Master_Thesis/eb_d.csv')
pd.DataFrame(b_c).to_csv('/home/fizlaz/bgse/Master_Thesis/b_c.csv')
pd.DataFrame(b_d).to_csv('/home/fizlaz/bgse/Master_Thesis/b_d.csv')

b_cum_c = aux.avg_bad_cum(control)
b_cum_d = aux.avg_bad_cum(cocaine)

pd.DataFrame(b_cum_c).to_csv('/home/fizlaz/bgse/Master_Thesis/b_cum_c.csv')
pd.DataFrame(b_cum_d).to_csv('/home/fizlaz/bgse/Master_Thesis/b_cum_d.csv')



##################################### parkinson

os.chdir('/home/fizlaz/bgse/Master_Thesis/hrvoje_new/')  

park_choice = pd.read_csv("parkinson_choices.csv").values.tolist()

e_park = aux.entropy(park_choice)

eb_park = aux.entropy_block(park_choice)

b_park = aux.avg_bad(park_choice)

b_cum_park = aux.avg_bad_cum(park_choice)

pd.DataFrame(e_park).to_csv('/home/fizlaz/bgse/Master_Thesis/e_park.csv')
pd.DataFrame(eb_park).to_csv('/home/fizlaz/bgse/Master_Thesis/eb_park.csv')
pd.DataFrame(b_park).to_csv('/home/fizlaz/bgse/Master_Thesis/b_park.csv')
pd.DataFrame(b_cum_park).to_csv('/home/fizlaz/bgse/Master_Thesis/b_cum_park.csv')

############### clustering cocaine

# Run computation 06
os.chdir('/home/fizlaz/bgse/Master_Thesis/hrvoje_new_extracted/cocaine/results/')


label = aux.rep(0,14) + aux.rep(1,12)


miner = data_clustering()
miner.prediction(choice_set = coc_data , entropy_set = ent , bad_set = bad,labelset = label,ent_block=ent_b, cluster_range = range(2,3), save = True)


miner.dframe.to_csv("cocaine2.csv")


############################## prison vs prison unbalanced, murder

c61 = aux.subset_data(choices,labels,[6,1])
c62 = aux.subset_data(choices,labels,[6,2])
c63 = aux.subset_data(choices,labels,[6,3])
c64 = aux.subset_data(choices,labels,[6,4])
c69 = aux.subset_data(choices,labels,[6,9])

e61 = aux.entropy(c61)
e62 = aux.entropy(c62)
e63 = aux.entropy(c63)
e64 = aux.entropy(c64)
e69 = aux.entropy(c69)

eb61 = aux.entropy_block(c61)
eb62 = aux.entropy_block(c62)
eb63 = aux.entropy_block(c63)
eb64 = aux.entropy_block(c64)
eb69 = aux.entropy_block(c69)

l61 = aux.labels(labels,[6,1],healthy=False)
l62 = aux.labels(labels,[6,2],healthy=False)
l63 = aux.labels(labels,[6,3],healthy=False)
l64 = aux.labels(labels,[6,4],healthy=False)
l69 = aux.labels(labels,[6,9],healthy=False)

b61 = aux.avg_bad(c61)
b62 = aux.avg_bad(c62)
b63 = aux.avg_bad(c63)
b64 = aux.avg_bad(c64)
b69 = aux.avg_bad(c69)


# Run computation 06 vs 01
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_01/')
miner = data_clustering()
miner.prediction(choice_set = c61 , entropy_set = e61 , bad_set = b61,labelset = l61,ent_block=eb61, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c61_b_cum_1.csv")

# Run computation 06 vs 02
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_02/')
miner = data_clustering()
miner.prediction(choice_set = c62 , entropy_set = e62 , bad_set = b62,labelset = l62,ent_block=eb62, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c62_b_cum_1.csv")

# Run computation 06 vs 03
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_03/')
miner = data_clustering()
miner.prediction(choice_set = c63 , entropy_set = e63 , bad_set = b63,labelset = l63,ent_block=eb63, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c63_b_cum_1.csv")

# Run computation 06 vs 04
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_04/')
miner = data_clustering()
miner.prediction(choice_set = c64 , entropy_set = e64 , bad_set = b64,labelset = l64,ent_block=eb64, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c64_b_cum_1.csv")

# Run computation 06 vs 09
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_09/')
miner = data_clustering()
miner.prediction(choice_set = c69 , entropy_set = e69 , bad_set = b69,labelset = l69,ent_block=eb69, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c69_b_cum_1.csv")




############################## prison vs prison balanced, murder

c1 = aux.subset_data(choices,labels,[1])
c2 = aux.subset_data(choices,labels,[2])
c3 = aux.subset_data(choices,labels,[3])
c4 = aux.subset_data(choices,labels,[4])
c6 = aux.subset_data(choices,labels,[6])
c9 = aux.subset_data(choices,labels,[9])


c61 = aux.subset_data(choices,labels,[6],c1)
c62 = aux.subset_data(choices,labels,[2],c6)
c63 = aux.subset_data(choices,labels,[6],c3)
c64 = aux.subset_data(choices,labels,[6],c4)
c69 = aux.subset_data(choices,labels,[9],c6)

e61 = aux.entropy(c61)
e62 = aux.entropy(c62)
e63 = aux.entropy(c63)
e64 = aux.entropy(c64)
e69 = aux.entropy(c69)

eb61 = aux.entropy_block(c61)
eb62 = aux.entropy_block(c62)
eb63 = aux.entropy_block(c63)
eb64 = aux.entropy_block(c64)
eb69 = aux.entropy_block(c69)

l61 = aux.labels(labels,[6],healthy=True)
l62 = aux.labels(labels,[2],healthy=True)
l63 = aux.labels(labels,[6],healthy=True)
l64 = aux.labels(labels,[6],healthy=True)
l69 = aux.labels(labels,[9],healthy=True)

b61 = aux.avg_bad(c61)
b62 = aux.avg_bad(c62)
b63 = aux.avg_bad(c63)
b64 = aux.avg_bad(c64)
b69 = aux.avg_bad(c69)


# Run computation 06 vs 01
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_01/')
miner = data_clustering()
miner.prediction(choice_set = c61 , entropy_set = e61 , bad_set = b61,labelset = l61,ent_block=eb61, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c61_b_cum_bal_1.csv")

# Run computation 06 vs 02
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_02/')
miner = data_clustering()
miner.prediction(choice_set = c62 , entropy_set = e62 , bad_set = b62,labelset = l62,ent_block=eb62, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c62_b_cum_bal_1.csv")

# Run computation 06 vs 03
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_03/')
miner = data_clustering()
miner.prediction(choice_set = c63 , entropy_set = e63 , bad_set = b63,labelset = l63,ent_block=eb63, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c63_b_cum_bal_1.csv")

# Run computation 06 vs 04
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_04/')
miner = data_clustering()
miner.prediction(choice_set = c64 , entropy_set = e64 , bad_set = b64,labelset = l64,ent_block=eb64, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c64_b_cum_bal_1.csv")

# Run computation 06 vs 09
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_09/')
miner = data_clustering()
miner.prediction(choice_set = c69 , entropy_set = e69 , bad_set = b69,labelset = l69,ent_block=eb69, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c69_b_cum_bal_1.csv")



############################## prison vs prison balanced, robbery

c1 = aux.subset_data(choices,labels,[1])
c2 = aux.subset_data(choices,labels,[2])
c3 = aux.subset_data(choices,labels,[3])
c4 = aux.subset_data(choices,labels,[4])
c6 = aux.subset_data(choices,labels,[6])
c9 = aux.subset_data(choices,labels,[9])


c21 = aux.subset_data(choices,labels,[2],c1)
c23 = aux.subset_data(choices,labels,[2],c3)
c24 = aux.subset_data(choices,labels,[2],c4)
c26 = aux.subset_data(choices,labels,[2],c6)
c29 = aux.subset_data(choices,labels,[2],c9)

e21 = aux.entropy(c21)
e23 = aux.entropy(c23)
e24 = aux.entropy(c24)
e26 = aux.entropy(c26)
e29 = aux.entropy(c29)

eb21 = aux.entropy_block(c21)
eb23 = aux.entropy_block(c23)
eb24 = aux.entropy_block(c24)
eb26 = aux.entropy_block(c26)
eb29 = aux.entropy_block(c29)

l21 = aux.labels(labels,[2],healthy=False) # didnt run like this, this not working
l23 = aux.labels(labels,[2],healthy=False)
l24 = aux.labels(labels,[2],healthy=False)
l26 = aux.labels(labels,[2],healthy=False)
l29 = aux.labels(labels,[2],healthy=False)

b21 = aux.avg_bad(c21)
b23 = aux.avg_bad(c23)
b24 = aux.avg_bad(c24)
b26 = aux.avg_bad(c26)
b29 = aux.avg_bad(c29)


# Run computation 02 vs 01
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_01/')
miner = data_clustering()
miner.prediction(choice_set = c21 , entropy_set = e21 , bad_set = b21,labelset = l21,ent_block=eb21, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c21_b_cum_bal_1.csv")

# Run computation 02 vs 03
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_03/')
miner = data_clustering()
miner.prediction(choice_set = c23 , entropy_set = e23 , bad_set = b23,labelset = l23,ent_block=eb23, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c23_b_cum_bal_1.csv")

# Run computation 02 vs 04
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_04/')
miner = data_clustering()
miner.prediction(choice_set = c24 , entropy_set = e24 , bad_set = b24,labelset = l24,ent_block=eb24, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c24_b_cum_bal_1.csv")

# Run computation 02 vs 06
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_06/')
miner = data_clustering()
miner.prediction(choice_set = c26 , entropy_set = e26 , bad_set = b26,labelset = l26,ent_block=eb26, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c26_b_cum_bal_1.csv")

# Run computation 02 vs 09
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_09/')
miner = data_clustering()
miner.prediction(choice_set = c29 , entropy_set = e29 , bad_set = b29,labelset = l29,ent_block=eb29, cluster_range = range(2,3), save = False)
miner.dframe.to_csv("c29_b_cum_bal_1.csv")





############################## prison vs prison unbalanced, robbery

c21 = aux.subset_data(choices,labels,[2,1])
c23 = aux.subset_data(choices,labels,[2,3])
c24 = aux.subset_data(choices,labels,[2,4])
c26 = aux.subset_data(choices,labels,[2,6])
c29 = aux.subset_data(choices,labels,[2,9])

e21 = aux.entropy(c21)
e23 = aux.entropy(c23)
e24 = aux.entropy(c24)
e26 = aux.entropy(c26)
e29 = aux.entropy(c29)

eb21 = aux.entropy_block(c21)
eb23 = aux.entropy_block(c23)
eb24 = aux.entropy_block(c24)
eb26 = aux.entropy_block(c26)
eb29 = aux.entropy_block(c29)

l21 = aux.labels(labels,[2,1],healthy=False)
l23 = aux.labels(labels,[2,3],healthy=False)
l24 = aux.labels(labels,[2,4],healthy=False)
l26 = aux.labels(labels,[2,6],healthy=False)
l29 = aux.labels(labels,[2,9],healthy=False)

b21 = aux.avg_bad(c21)
b23 = aux.avg_bad(c23)
b24 = aux.avg_bad(c24)
b26 = aux.avg_bad(c26)
b29 = aux.avg_bad(c29)

############################## check labels and whether to do unbalanced



#############################looping

frame_list=[]

for i in range(20):

	print "\n"
	print "#  #  #  #  #  #  #  #  #  #  #  #  "
	print "Started with iteration \t " + str(i)
	print "#  #  #  #  #  #  #  #  #  #  #  #  "


	# Mean of the bandits 
	p01 = aux.rep([0,1,2],6)
	# Standard Deviation of the bandits
	p02 = aux.rep([1,1,1],6)
	# Set of number of trials 
	p03 = aux.rep(100,6)
	# Set of size of clusters	
	p04 = aux.rep(10,6)

	# Set of decision functions
	p06 = aux.rep("softmax",6)

	
	# Set of alphas
	p07 = aux.rep([1,1], 6 )

	# Set of Taus
	tau = [ [0.1,0.3], [0.1,0.5], [0.1,0.7],
			[0.1,1], [0.1,1.5], [0.1,2] ] 	
	
	"""
	tau=aux.rep([1,1],6)

	p07 = [[0.1,0.3], [0.1,0.5], [0.1,0.7],
		   [0.1,0.9], [0.5,0.9], [0.7,0.9]]
	"""

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
									  iowa = False
									 )

	frame_list.append(prediction_accuracies.dframe)


cols = ["mut inf scr","adj mis","norm mis","adj rand s","complet","homogen","vmeas"]
avg_frame = aux.summary_df(frame_list,cols)

avg_frame.round(5).to_csv("../Results/Simulation_repeated/data_mean1_a_10_t_50_1.csv")

print avg_frame




############## means

os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Simulation_repeated/')

file = "data_mean2_a_t_10_50_1.csv"


os.chdir("/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/")

file = "06_02/06vs02_average_looper1.csv"

aux.block_means(file)







#############################looping

frame_list=[]

for i in range(20):
	
	print "\n"
	print "#  #  #  #  #  #  #  #  #  #  #  #  "
	print "Started with iteration \t " + str(i)
	print "#  #  #  #  #  #  #  #  #  #  #  #  "
	
	# Run computation 06 vs 01
	miner = data_clustering()
	miner.prediction(choice_set = c61 , entropy_set = e61 , bad_set = b61,labelset = l61,ent_block=eb61, cluster_range = range(2,3), save = False)
	
	frame_list.append(miner.dframe)


os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_01/')

cols = ['mut inf scr', 'adj mis','norm mis', 'adj rand s', 'complet', 'homogen', 'vmeas']

sub01 = frame_list[0].ix[:,:2]
sub02 = aux.statistics_df(frame_list,cols)
avg_frame = pd.concat([sub01,sub02],axis=1)
avg_frame.to_csv("06vs01_average.csv")


miner1=data_clustering_looping()
miner1.prediction(choice_set = c61 , entropy_set = e61 , bad_set = b61,labelset = l61,ent_block=eb61, cluster_range = range(2,3), save = False)

frame_list1 = miner1.dframe

cols = ['mut inf scr', 'adj mis','norm mis', 'adj rand s', 'complet', 'homogen', 'vmeas']

sub01 = frame_list1[0].ix[:,:2]
sub02 = aux.statistics_df(frame_list1,cols)
avg_frame = pd.concat([sub01,sub02],axis=1)
avg_frame.to_csv("06vs01_average_domlooper1.csv")



################## this was run on unbalanced


os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_01/')
miner2 = data_clustering_looping()
miner2.prediction(choice_set = c61 , entropy_set = e61 , bad_set = b61,labelset = l61,ent_block=eb61, cluster_range = range(2,3), save = False)
avg_frame = miner2.avg_frame
avg_frame.to_csv("06vs01_average_domlooper2.csv")


os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_02/')
miner2 = data_clustering_looping()
miner2.prediction(choice_set = c62 , entropy_set = e62 , bad_set = b62,labelset = l62,ent_block=eb62, cluster_range = range(2,3), save = False)
avg_frame = miner2.avg_frame
avg_frame.to_csv("06vs02_average_looper1.csv")


os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_03/')
miner2 = data_clustering_looping()
miner2.prediction(choice_set = c63 , entropy_set = e63 , bad_set = b63,labelset = l63,ent_block=eb63, cluster_range = range(2,3), save = False)
avg_frame = miner2.avg_frame
avg_frame.to_csv("06vs03_average_looper1.csv")


os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_04/')
miner2 = data_clustering_looping()
miner2.prediction(choice_set = c64 , entropy_set = e64 , bad_set = b64,labelset = l64,ent_block=eb64, cluster_range = range(2,3), save = False)
avg_frame = miner2.avg_frame
avg_frame.to_csv("06vs04_average_looper1.csv")


os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/06_vs_rest/06_09/')
miner2 = data_clustering_looping()
miner2.prediction(choice_set = c69 , entropy_set = e69 , bad_set = b69,labelset = l69,ent_block=eb69, cluster_range = range(2,3), save = False)
avg_frame = miner2.avg_frame
avg_frame.to_csv("06vs09_average_looper1.csv")



########################### 2 vs all unbalanced looper


# Run computation 02 vs 01
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_01/')
miner = data_clustering_looping()
miner.prediction(choice_set = c21 , entropy_set = e21 , bad_set = b21,labelset = l21,ent_block=eb21, cluster_range = range(2,3), save = False)
miner.avg_frame.to_csv("02vs01_average_unbal_looper1.csv")

# Run computation 02 vs 03
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_03/')
miner = data_clustering_looping()
miner.prediction(choice_set = c23 , entropy_set = e23 , bad_set = b23,labelset = l23,ent_block=eb23, cluster_range = range(2,3), save = False)
miner.avg_frame.to_csv("02vs03_average_unbal_looper1.csv")

# Run computation 02 vs 04
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_04/')
miner = data_clustering_looping()
miner.prediction(choice_set = c24 , entropy_set = e24 , bad_set = b24,labelset = l24,ent_block=eb24, cluster_range = range(2,3), save = False)
miner.avg_frame.to_csv("02vs04_average_unbal_looper1.csv")

# Run computation 02 vs 06
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_06/')
miner = data_clustering_looping()
miner.prediction(choice_set = c26 , entropy_set = e26 , bad_set = b26,labelset = l26,ent_block=eb26, cluster_range = range(2,3), save = False)
miner.avg_frame.to_csv("02vs06_average_unbal_looper1.csv")

# Run computation 02 vs 09
os.chdir('/home/fizlaz/bgse/Master_Thesis/Master_Project_Felix/Work/Code and Analysis/Results/Real data/02_vs_rest/02_09/')
miner = data_clustering_looping()
miner.prediction(choice_set = c29 , entropy_set = e29 , bad_set = b29,labelset = l29,ent_block=eb29, cluster_range = range(2,3), save = False)
miner.avg_frame.to_csv("02vs09_average_unbal_looper1.csv")










