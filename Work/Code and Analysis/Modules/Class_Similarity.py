class similarity:

	"""
	SET INITIAL CONDITIONS
	Requires import numpy as np
	"""
	def __init__(self):	

		# Categorical similarity meassures
		self.overlap = None
		self.cosine_cat = None
		self.eskin_sim = None
		self.lin_sim = None
		self.eskin_disim = None
		self.lin_disim = None

		# Time series
		self.euclidian = None
		self.edtw = None
		self.euclidian_dist = None
		self.cosine_ent = None
		self.rbf = None
		self.edr_sim = None

	"""
	Conpute functions
	"""

	# Computes similarities for categorical data
	def categorical(self,data ):

		self.overlap = self.overlap_similarity( data = data )
		self.cosine_cat = self.cosine_similarity(data = data)
		self.eskin_sim = self.eskin_similarity(data=data)
		self.lin_sim = self.lin_similarity(data=data)
		self.eskin_disim = self.eskin_dissimilarity(data=data)
		self.lin_disim = self.lin_dissimilarity(data=data)

	# Computes similarities for time series and real valued data
	def timeseries(self, data ):
		self.euclidian = self.euclidian_similiarity( data = data )
		self.edtw = self.euclidian_time_warp_similarity( data = data )
		self.euclidian_dist = self.euclidian_distance( data, data )
		self.cosine_ent = self.cosine_similarity(data = data)
		self.rbf = self.rbf_similarity(data=data)
		self.edr_sim = self.edr_similarity(data,0.1)

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

	def edr_similarity(self,data,eps):
		dist = self.pairwise_distance( data, self.edr, eps )
		edit_distance_on_real_sequence = self.similarity(dist)
		return edit_distance_on_real_sequence

	def rbf_similarity(self,data):
		similarity = pa.rbf_kernel(data)
		return similarity

	def cosine_similarity(self,data):
		similarity = pa.cosine_similarity(data)
		return similarity

	def levenstein_similarity(self,data):
		dist = self.pairwise_distance( list_of_list = data, distance_function = self.levenstein_distance )
		levenstein_similarity = self.similarity(dist)
		return levenstein_similarity

	def eskin_similarity(self,data):
		similarity = self.similarity(self.eskin_dissimilarity(data))
		return similarity

	def lin_similarity(self,data):
		similarity = self.similarity(self.lin_dissimilarity(data))
		return similarity

	def eskin_dissimilarity(self,data):
		frame = np.vstack((data))
		r = frame.shape[0]
		s = frame.shape[1]

		#recording variables
		num_var = frame.shape[1]
		num_row = frame.shape[0]
		data2 = np.zeros((num_row, num_var))
		for k in range(num_var):
			categories = np.unique(frame[:,k])
			cat_new = range(len(categories))
			for l in range(len(categories)):
				for i in range(num_row):
					if frame[i,k] == categories[l]:
						data2[i,k] = cat_new[l] +1

		frame = data2

		num_cat = np.apply_along_axis(self.my_unique,0,frame)

		agreement = np.zeros(s)
		eskin = np.zeros((r,r))

		for i in range(r):
			for j in range(r):
				for k in range(s):
					if frame[i,k] == frame[j,k]:
						agreement[k] = 1
					else:
						agreement[k] = float(num_cat[k]**2) / (num_cat[k]**2 +2)
				
				eskin[i,j] = float(1) / ( (float(1) / s*sum(agreement)) ) - 1
		
		return eskin

	def lin_dissimilarity(self,data):
		frame = np.vstack((data))
		r = frame.shape[0]
		s = frame.shape[1]

		#recording variables
		num_var = frame.shape[1]
		num_row = frame.shape[0]
		data2 = np.zeros((num_row, num_var))
		for k in range(num_var):
			categories = np.unique(frame[:,k])
			cat_new = range(len(categories))
			for l in range(len(categories)):
				for i in range(num_row):
					if frame[i,k] == categories[l]:
						data2[i,k] = cat_new[l] + 1

		frame = data2

		freqabs = self.freq_abs(frame)
		freqrel = freqabs / float(r)

		agreement = np.zeros(s)
		lin = np.zeros((r,r))
		weights = np.zeros(s)

		for i in range(int(r)):
			for j in range(int(r)):
				for k in range(int(s)):
					c = frame[i,k] -1
					d = frame[j,k] -1
					if frame[i,k] == frame[j,k]:
						agreement[k] = 2*np.log(freqrel[c,k])
					else:
						agreement[k] = 2*np.log(freqrel[c,k] + freqrel[d,k])
					weights[k] = np.log(freqrel[c,k]) + np.log(freqrel[d,k])

				if i == j:
					lin[i,j] = 0
				else:
					lin[i,j]=float(1)/ (float(1) / sum(weights)*sum(agreement) ) -1

		return lin


	"""
	Pairwise distance functions
	"""
	# 1) Categorical Data

	# Overlap distance computes same items in point X and point Y
	# Expects two NumPy arrays
	def overlap_distance( self, X , Y ):
		overlap_distance = sum( X == Y )
		return overlap_distance

	def levenstein_distance(self,X,Y):
		dist = editdistance.eval(X, Y)
		return dist

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

	# Edit Distance on Real sequence
	def edr(self, X,Y, eps ):
		m = len(X)
		n = len(Y)
		C = np.zeros(shape=( m + 1, n + 1))
		for i in range(1,m+1):
			for j in range(1, n+1):
				temp_x = X[i-1]
				temp_y = Y[j-1]
				temp_norm = self.norm( temp_x, temp_y )
			if temp_norm < eps:
				cost = 0
			else:
				cost = 1
			C[i][j] = min(C[i][j-1]+1, C[i-1][j]+1,C[i-1][j-1]+cost)
		final_edr = float(C[m][n])/max([m,n])
		return final_edr  

	"""
	Auxilliary functions
	"""

	# Computes a pairwise distance matrix according to distance function
	# Implementation is not efficient. Might be slow for big data sets
	def pairwise_distance(self, list_of_list, distance_function, *args ):
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
				if not args:
					val =  distance_function(temp_node_i , temp_node_j)
				else:
					argument = args[0]
					val =  distance_function(temp_node_i , temp_node_j,argument)
				distance_matrix[i,j] = val
				distance_matrix[j,i] = val
				j = j + 1
			i = i + 1
			j = i + 1
		return distance_matrix

	def my_unique(self,x):
		u = np.unique(x)
		l = len(u)
		return l

	def freq_abs(self,frame):
		r = frame.shape[0]
		s = frame.shape[1]

		freq_table = np.zeros((max(np.unique(frame)),s))

		for i in range(int(s)):
			for j in range( int(max(frame[:,i])) ):
				count = []
				for k in range(int(r)):
					if frame[k,i] == j+1:
						count.append(1)
					else:
						count.append(0)

				freq_table[j,i] = sum(count)

		return freq_table

	# Convertes a distance matrix to a similarity matrix
	def similarity(self, distance_matrix ):
		similarity_matrix = float(1) / ( 1 + distance_matrix )
		return similarity_matrix

	# Convertes a similarity matrix to a dissimliarty (proximity) matrix
	def dissimilarity(self,similarity_matrix):
		dissimilarity_matrix = float(1) / ( similarity_matrix - 1 )
		np.fill_diagonal(dissimilarity_matrix, 0)
		return dissimilarity_matrix

	def norm(self,x,y):
		result = np.linalg.norm(x-y)
		return result




