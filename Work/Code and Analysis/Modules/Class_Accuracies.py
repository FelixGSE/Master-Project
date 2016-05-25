class accuracies:

	"""
	Set initial conditions
	Requires:
	import sklearn.metrics.cluster as mclu
	"""

	def __init__(self, true_label = None, prediction = None):

		# Define self true label and prediction
		self.true = true_label
		self.prediction = prediction
		
		# Check input specification
		if self.true == None or self.prediction == None:
			raise ValueError("Class Accuracies requires a vector of true labels and predictions")
		if len( self.true ) is not len( self.prediction ):
			raise ValueError("Vectors must have the same length")

		# Compute accuracy meassures 
		self.amis = self.amis(self.true,self.prediction)
		self.ars = self.adjusted_rand_score(self.true,self.prediction)
		self.completness = self.completeness_score(self.true,self.prediction)
		self.hcvm = self.homogeneity_completeness_v_measure(self.true,self.prediction)
		self.homogenity = self.homogeneity_score(self.true,self.prediction)
		self.mis = self.mutual_info_score(self.true,self.prediction)
		self.nmis = self.normalized_mutual_info_score(self.true,self.prediction)
		#self.sscore = self.silhouette_score(self.true,self.prediction)
		#self.samples = self.silhouette_samples(self.true,self.prediction)
		self.vmeasure = self.v_measure_score(self.true,self.prediction)
		self.full = [ self.mis, self.amis, self.nmis, self.ars , self.completness, self.homogenity , self.vmeasure ]

	"""
	Accuracy meassures
	"""

	# 1) Confusion matrix 
	def amis(self, true, pred ):
		metric = mclu.adjusted_mutual_info_score(true, pred)
		return metric

	# 2) Adjusted Rand Score 
	def adjusted_rand_score(self, true, pred  ):
		metric = mclu.adjusted_rand_score(true, pred)
		return metric 

	# 3) Completnes Score 
	def completeness_score(self, true, pred  ):
		metric = mclu.completeness_score(true, pred)
		return metric 
		
	# 4) Homogeneity Completeness V Measure
	def homogeneity_completeness_v_measure( self, true,pred ):
		metric = mclu.homogeneity_completeness_v_measure( true, pred)
		return metric

	# 5) Homogeneity Score
	def homogeneity_score(self, true,pred ):
		metric = mclu.homogeneity_score(true, pred)
		return metric

	# 6) Mutual info score
	def mutual_info_score(self, true,pred ):
		metric = mclu.mutual_info_score(true, pred)
		return metric

	# 7) Normalized Mutual info score
	def normalized_mutual_info_score(self, true,pred ):
		metric = mclu.normalized_mutual_info_score(true, pred)
		return metric 

	# 8) Silhouette Score
	#def silhouette_score(self, true,pred ):
	#	metric = mclu.silhouette_score(true, pred)
	#	return metric

	# 9) Silhouette Samples
	def silhouette_samples(self, true,pred ):
		metric = mclu.silhouette_samples(true, pred)
		return metric

	# 10) V Measure Score
	def v_measure_score(self, true,pred ):
		metric = mclu.v_measure_score(true, pred)
		return metric

	# Print a formated report of all accuracies
	def report_accuracies(self,full = False):
		print '\n'
		print '*********************************************'
		print 'Accuraccy report'
		print '*********************************************'
		print 'Adjusted Mutual Info Score: \t\t\t' + str(self.out(self.amis))
		print '---------------------------------------------'
		print 'Adjusted Rand Score: \t \t \t\t\t' + str(self.out(self.ars))
		print '---------------------------------------------'
		print 'Completeness Score: \t \t \t\t\t' + str(self.out(self.completness))
		print '---------------------------------------------'
		#print 'Homogeneity Completeness V Measure : \t' + str(self.out(self.hcvm))
		#print '---------------------------------------------'
		print 'Homogeneity Score: \t\t\t\t\t\t' + str(self.out(self.homogenity))
		print '---------------------------------------------'
		print 'Mutual info score: \t\t\t\t\t\t' + str(self.out(self.mis))
		print '---------------------------------------------'
		print 'Nomailzed Mutual info score: \t\t\t' + str(self.out(self.nmis))
		print '---------------------------------------------'
		#print 'Silhouette Score: \t\t\t' + str(self.out(self.sscore))
		#print '---------------------------------------------'
		#print 'Silhouette Samples: \t\t\t' + str(self.out(self.samples))
		#print '---------------------------------------------'
		print 'V Measure Score: \t\t\t\t\t\t' + str(self.out(self.vmeasure))
		print '---------------------------------------------'
		print '*********************************************'
		print '\n'
	# Round numbers
	def out(self,number):
		round = format(number, '.3f')
		return round

	def round_list(self,list):
		new = []
		for item in list:
			try:
				temp = self.out(item)
			except:
				temp = None
			new.append(temp)
		return new