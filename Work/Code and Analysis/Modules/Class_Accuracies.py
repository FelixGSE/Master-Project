class accuracies:

	"""
	Set initial conditions
	Requires:
	import sklearn.metrics as met
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
		self.confusion_matrix = self.confusion_matrix( self.true, self.prediction )
		self.accuracy = self.accuracy( self.true, self.prediction  )
		self.f1score = self.f1( self.true, self.prediction )
		self.hamming = self.hamming( self.true, self.prediction )
		self.jaccard = self.jaccard( self.true, self.prediction )
		self.prfs = self.prfs( self.true, self.prediction )
		self.ps = self.ps( self.true, self.prediction  )
		self.recall = self.recall_score( self.true, self.prediction )
		self.zeroone = self.zero_one_loss( self.true, self.prediction )

	"""
	Accuracy meassures
	"""

	# 1) Confusion matrix 
	def confusion_matrix(self, true, pred ):
		confusion_matrix = met.confusion_matrix( true, pred )
		return confusion_matrix

	# 2) Accuracy 
	def accuracy(self, true, pred ):
		accuracy = met.accuracy_score( true, pred )
		return accuracy

	# 3) f1 Score
	def f1(self,true,pred):
		f01 = met.f1_score( true, pred, average = 'macro') 
		f02 = met.f1_score( true, pred, average = 'micro') 
		f03 = met.f1_score( true, pred, average = 'weighted') 
		f04 = met.f1_score( true, pred, average = None )
		f1_list = [f01,f02,f03,f04]
		return f1_list

	# 4) Hamming Loss
	def hamming( self,true,pred ):
		hamming_loss = met.hamming_loss(true, pred)
		return hamming_loss

	# 5) Jaccard Similarity Score	
	def jaccard( self,true,pred ):
		jaccard_similarity_score = met.jaccard_similarity_score(true, pred)
		return jaccard_similarity_score

	# 6) Precision Recall Fscore Support
	def prfs( self,true,pred ):
		prfs01 = met.precision_recall_fscore_support(true, pred, average = 'macro')
		prfs02 = met.precision_recall_fscore_support(true, pred, average = 'micro')
		prfs03 = met.precision_recall_fscore_support(true, pred, average = 'weighted')
		prfs_list = [prfs01,prfs02,prfs03]
		return prfs_list

	# 7) Precision Score 
	def ps( self,true,pred ):
		ps01 = met.precision_score(true, pred, average = 'macro')
		ps02 = met.precision_score(true, pred, average = 'micro') 
		ps03 = met.precision_score(true, pred, average = 'weighted') 
		ps_list = [ps01,ps02,ps03]
		return ps_list

	# 8) Recall Score
	def recall_score( self,true,pred ):
		recall01 = met.recall_score(true, pred, average = 'macro') 
		recall02 = met.recall_score(true, pred, average = 'micro') 
		recall03 = met.recall_score(true, pred, average = 'weighted') 
		recall04 = met.recall_score(true, pred, average = None) 
		recall_list = [recall01,recall02,recall03,recall04]
		return recall_list

	# 9) Zero-One-Loss
	def zero_one_loss( self,true,pred ):
		zero_one = met.zero_one_loss(true, pred)
		return zero_one

	"""
	Auxilliary functions
	"""

	# Print a formated report of all accuracies
	def report_accuracies(self,full = False):
		print '*********************************'
		print 'Accuraccy report'
		print '*********************************'
		print 'Accuracy: \t \t \t \t \t' + str(self.out(self.accuracy))
		print '---------------------------------'
		print 'Hamming Loss:\t \t \t \t' + str(self.out( self.hamming))
		print '---------------------------------'
		print 'Jaccard Similarity Score: \t' + str(self.out( self.jaccard))
		print '---------------------------------'
		print 'Zero-One-Loss:\t \t \t \t' + str(self.out( self.zeroone))
		print '---------------------------------'
		print 'F1-Score'
		print ''.ljust(2) + 'Macro:\t \t \t \t \t' + str(self.out( self.f1score[0]) )
		print ''.ljust(2) + 'Micro:\t \t \t \t \t' + str(self.out( self.f1score[1]) )
		print ''.ljust(2) + 'Weighted:\t \t \t \t \t' + str(self.out( self.f1score[2]) )
		print '---------------------------------'
		print 'Precision Score '
		print ''.ljust(2) + 'Macro:\t \t \t \t \t' + str(self.out( self.ps[0]) )
		print ''.ljust(2) + 'Micro:\t \t \t \t \t' + str(self.out( self.ps[1]) )
		print ''.ljust(2) + 'Weighted:\t \t \t \t \t' + str(self.out( self.ps[2]) )
		print '---------------------------------'
		print 'Recall Score '
		print ''.ljust(2) + 'Macro:\t \t \t \t \t' + str(self.out( self.recall[0]) )
		print ''.ljust(2) + 'Micro:\t \t \t \t \t' + str(self.out( self.recall[1]) )
		print ''.ljust(2) + 'Weighted:\t \t \t \t \t' + str(self.out( self.recall[2]) )
		if full == True:
			print '---------------------------------'
			print 'Precision Recall Fscore Support'
			print 'Macro'
			print str(self.round_list(self.prfs[0]))
			print 'Micro'
			print str(self.round_list(self.prfs[1]))
			print 'Weighted'
			print str(self.round_list(self.prfs[2]))
		print '*********************************'


	def report_matrix(self):
		print '*********************************'
		print 'Confusion matrix'
		print '*********************************'
		print self.confusion_matrix
		print '*********************************'

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