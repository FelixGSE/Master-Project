class unsupervised:

	"""
	Initial conditions
	"""
	def __init__(self, data = None,n = 3):
		self.n = None

	"""
	Call all
	"""
	def fit_all_with_affinity(self, data, n = None):
	 	
	 	if n == None:
	 		n = self.n

	 	self.spectral_prediction = self.spectral( data = data, n_clust = n )
	 	self.affinity_prediction = self.affinity_propagation( data = data )

	def


	"""
	Clustering functions
	"""
	def spectral(self, data, n_clust, affinity = 'precomputed'):
	 	spectral = clu.SpectralClustering(n_clusters=n_clust,affinity = affinity)
	 	spectral.fit_predict(data)
	 	predictions = spectral.labels_
	 	return predictions

	def affinity_propagation(self, data,affinity = 'precomputed'):
	 	affity_prop = clu.AffinityPropagation(affinity= affinity)
	 	affity_prop.fit_predict(data)
	 	predictions = affity_prop.labels_
	 	return predictions

	def kmeans(self,data,nclust=3,init = 20, seed=None ):
	 	kmean = clu.KMeans(n_clusters = nclust,n_init=init,random_state=seed)
	 	kmean.fit_predict(data)
	 	prediction = kmean.labels_
	 	return prediction

	def db_scan(self, data, distance = 0.5, affinity = "precomputed"):
	 	scan = clu.DBSCAN(eps = distance, metric = affinity)
	 	scan.fit_predict(data)
	 	prediction = scan.labels_
	 	return prediction

	def ward_clustering(self, data, nclust=3, affinity='euclidean'):
		ward = clu.AgglomerativeClustering(n_clusters = nclust, affinity = affinity, linkage ='ward' )
		ward.fit_predict(data)
		prediction = ward.labels_
		return prediction
	
	def complete_hierachical(self, data, nclust=3, affinity='precomputed' ):
		complete = clu.AgglomerativeClustering(n_clusters = nclust, affinity = affinity, linkage ='complete' )
		complete.fit_predict(data)
		prediction = complete.labels_
		return prediction

	def average_hierachical(self, data, nclust=3, affinity='precomputed' ):
		average = clu.AgglomerativeClustering(n_clusters = nclust, affinity = affinity, linkage ='average' )
		average.fit_predict(data)
		prediction = average.labels_
		return prediction

	def pca(self, data, n = 3):
		principal_components = decomp.PCA(n_components=n)
		principal_components.fit( data )
		variance = principal_components.explained_variance_ratio_
		components = principal_components.components_
		output = [variance,components]
		return output

	def pca_ward(self,data,nclus = 3, ncomp = 3):
		pc = self.pca(data, n = ncomp)[1]
		cluster = self.ward_clustering(data,nclust = nclus )
		return cluster





"""
TESTING AREA 
test = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[1010,1010,1010,1010],[1000000000,1000000000,1000000000,100000000]]
se = similarity()
s = se.euclidian_distance(test,test)
import sklearn.cluster as clu
import sklearn.decomposition as decomp
us = unsupervised().complete_hierachical(s,3)
print us

print pca.explained_variance_ratio_
"""
