####################################################################################################

####################################################################################################

### Load Modules
import random as rd
import numpy as np
import os 
import json
import time
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
### Source own modules
path_data = "/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Artificial Data Sets/d01/"
os.chdir(path_data)  

# Load Data
with open('choicessoftmax_19_32_31.txt') as data_file:    
    data = json.load(data_file)

####################################################################################################

####################################################################################################

X = np.array(data)
random_state = 170
y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)


####################################################################################################

####################################################################################################


