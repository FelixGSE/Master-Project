class similarity:

	"""
	SET INITIAL CONDITIONS
	Requires import numpy as np
	"""
	def __init__(self):	

		# Categorical similarity meassures
		self.overlap = None

		# Time series
		self.euclidian = None
		self.edtw = None

	"""
	Conpute functions
	"""

	# Computes similarities for categorical data
	def categorical(self,data ):

		self.overlap = self.overlap_similarity( data = data )

	# Computes similarities for time series and real valued data
	def timeseries(self, data ):
		self.euclidian = self.euclidian_similiarity( data = data )
		self.edtw = self.euclidian_time_warp_similarity( data = data )
		self.euclidian_dist = self.euclidian_distance( data, data )

	"""
	Similarity functions
	"""

	# Computes overlap similarity between to points
	def overlap_similarity( self, data ):
		dist = self.pairwise_distance( list_of_list = data, distance_function = self.overlap_distance )
		overlap_similarity = self.similarity(dist)
		return overlap_similarity

	# Computes euclidian similarity
	def euclidian_similiarity(self, data ):
		dist = self.euclidian_distance( data, data )
		euclidian_similiarity = self.similarity(dist)
		return euclidian_similiarity

	def euclidian_time_warp_similarity(self,data):
		dist = self.pairwise_distance( list_of_list = data, distance_function = self.time_warp_euclidian_distance )
		euclidian_time_warp_similarity = self.similarity(dist)
		return euclidian_time_warp_similarity

	"""
	Pairwise distance functions
	"""
	# 1) Categorical Data

	# Overlap distance computes same items in point X and point Y
	# Expects two NumPy arrays
	def overlap_distance( self, X , Y ):
		overlap_distance = sum( X == Y )
		return overlap_distance

	# 2) Time series and real-valued data

	# Euclidian Distance
	def euclidian_distance( self, X, Y):
		dist = pa.euclidean_distances(X,Y)
		return dist

	# Time warp distance for two time series X and Y with metric
	def time_warp_euclidian_distance(self,X,Y):
		X = np.array(X).reshape(-1, 1)
		Y = np.array(Y).reshape(-1, 1)
		dist = dtw.dtw(X, Y, dist = lambda X, Y: np.linalg.norm(X - Y, ord=2))[0]
		return dist

	"""
	Auxilliary functions
	"""

	# Computes a pairwise distance matrix according to distance function
	# Implementation is not efficient. Might be slow for big data sets
	def pairwise_distance(self, list_of_list, distance_function ):
		dimensions = len( list_of_list )
		i = 0
		j = i + 1
		distance_matrix = np.zeros((dimensions, dimensions))
		np.fill_diagonal(distance_matrix, 0)
		array = np.array(list_of_list)
		while i < (dimensions - 1):
			temp_node_i = array[i,]
			while j < dimensions:
				temp_node_j = array[j,]
				val =  distance_function(temp_node_i , temp_node_j)
				distance_matrix[i,j] = val
				distance_matrix[j,i] = val
				j = j + 1
			i = i + 1
			j = i + 1
		return distance_matrix

	# Convertes a distance matrix to a similarity matrix
	def similarity(self, distance_matrix ):
		similarity_matrix = float(1) / ( 1 + distance_matrix )
		return similarity_matrix

	# Convertes a similarity matrix to a dissimliarty (proximity) matrix
	def dissimilarity(self,similarity_matrix):
		dissimilarity_matrix = float(1) / ( similarity_matrix - 1 )
		np.fill_diagonal(dissimilarity_matrix, 0)
		return dissimilarity_matrix







