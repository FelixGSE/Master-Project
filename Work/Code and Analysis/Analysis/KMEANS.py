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
import sklearn.metrics as met

### Source own modules
path_data = "/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Artificial Data Sets/d01/"
os.chdir(path_data)  

# Load Data
with open('choicessoftmax_19_32_31.txt') as data_file:    
    data = json.load(data_file)

####################################################################################################

####################################################################################################

# No transformation
X = np.array(data)
kmeans = KMeans(n_clusters = 2, max_iter = 500, n_init = 20 )
ypred = kmeans.fit_predict(X, y = None)











####################################################################################################
# Arguments
####################################################################################################

"""
n_clusters : int, optional, default: 8
The number of clusters to form as well as the number of centroids to generate.
max_iter : int, default: 300
Maximum number of iterations of the k-means algorithm for a single run.
n_init : int, default: 10
Number of time the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n_init consecutive runs in terms of inertia.
init : {‘k-means++’, ‘random’ or an ndarray}
Method for initialization, defaults to ‘k-means++’:
‘k-means++’ : selects initial cluster centers for k-mean clustering in a smart way to speed up convergence. See section Notes in k_init for more details.
‘random’: choose k observations (rows) at random from data for the initial centroids.
If an ndarray is passed, it should be of shape (n_clusters, n_features) and gives the initial centers.
precompute_distances : {‘auto’, True, False}
Precompute distances (faster but takes more memory).
‘auto’ : do not precompute distances if n_samples * n_clusters > 12 million. This corresponds to about 100MB overhead per job using double precision.
True : always precompute distances
False : never precompute distances
tol : float, default: 1e-4
Relative tolerance with regards to inertia to declare convergence
n_jobs : int
The number of jobs to use for the computation. This works by computing each of the n_init runs in parallel.
If -1 all CPUs are used. If 1 is given, no parallel computing code is used at all, which is useful for debugging. For n_jobs below -1, (n_cpus + 1 + n_jobs) are used. Thus for n_jobs = -2, all CPUs but one are used.
random_state : integer or numpy.RandomState, optional
The generator used to initialize the centers. If an integer is given, it fixes the seed. Defaults to the global numpy random number generator.
verbose : int, default 0
Verbosity mode.
copy_x : boolean, default True
When pre-computing distances it is more numerically accurate to center the data first. If copy_x is True, then the original data is not modified. If False, the original data is modified, and put back before 
the function returns, but small numerical differences may be introduced by subtracting and then adding the data mean.
"""
