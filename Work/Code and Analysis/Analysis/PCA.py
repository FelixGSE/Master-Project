####################################################################################################

####################################################################################################

### Load Modules
import random as rd
import numpy as np
import os 
import json
import time
from sklearn.decomposition import PCA

### Source own modules
path_data = "/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Artificial Data Sets/d01/"
os.chdir(path_data)  

# Load Data
with open('choicessoftmax_19_32_31.txt') as data_file:    
    data = json.load(data_file)

####################################################################################################

####################################################################################################

# Example from website
X = np.array(data)
pca = PCA(n_components=2)
pca.fit(X)
PCA(copy=True, n_components=2, whiten=False)
print(pca.explained_variance_ratio_) 







####################################################################################################

####################################################################################################
