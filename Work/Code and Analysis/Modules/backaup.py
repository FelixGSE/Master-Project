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