class miner:

	def __init__(self):

		self.accuracy_set = []


	def prediction(self, mu_set, sigma_set,N_set,cluster_set,seed_set,decision_function_set,alpha_set,tau_set,epsilon_set = None, iowa = False):

		# Detect runtime by computing the number of mean sets
		runtime = range(len(mu_set))

		# Set column names for final data frame
		column_names=["mu","sigma","trials","cluster size","decision","alpha","tau","epsilon",\
			"clustering","labels","mut inf scr","adj mis","norm mis","adj rand s","complet","homogen","vmeas",\
			"mut inf scr1","adj mis1","norm mis1","adj rand s1","complet1","homogen1","vmeas1"]

		column_names_1=["mut inf scr","adj mis","norm mis","adj rand s","complet","homogen","vmeas"]

		# Intialize final data frame
		dframe = pd.DataFrame(columns=column_names)
		dframe1 = pd.DataFrame(columns=column_names_1)

		aux = auxilliary()

		for step in runtime:

			# Print trace
			print "\n"
			print "*************************************"
			print "Started with iteration \t " + str(step)
			print "-------------------------------------"

			# Subset for current iteration  
			mu = mu_set[step]
			sigma = sigma_set[step]
			N = N_set[step]
			cluster = cluster_set[step]
			seed = None
			decision_function = decision_function_set[step]
			alpha = alpha_set[step]
			if tau_set == None:
				tau = None
			else:
				tau = tau_set[step]
				param = tau_set[step]
			if epsilon_set == None:
				epsilon = None
			else:
				epsilon = epsilon_set[step]
				param = tau_set[step]

			# Create data set
			temp_data = data()
			temp_data.create_data( individual = True, mu = mu, sigma = sigma, N = N,
							cluster_size = cluster, seed = seed, decision_function = decision_function, 
							alpha = alpha, tau = tau, epsilon =  epsilon, iowa=iowa)

			# Extract features from current data set
			temp_entropy = temp_data.entropies
			temp_choices = temp_data.choices 
			temp_labels  = temp_data.label
			temp_concats = temp_data.concat
			
			##
			bad_set = aux.avg_bad_multi(temp_choices)
			ent_block = aux.entropy_block(temp_choices)

			# Compute Similarities - Begin Trace	
			print "*************************************"
			print "Start computing similarity"
			print "-------------------------------------"

			# Compute Similarities
			sim = similarity()
			sim.timeseries(temp_entropy)
			sim.categorical(temp_choices)
			temp_timewarp = sim.edtw
			temp_eucliddist = sim.euclidian_dist
			temp_overlap = sim.overlap
			cosine_cat = sim.cosine_cat
			cosine_ent = sim.cosine_ent
			rbf = sim.rbf
			eskin_sim = sim.eskin_sim
			lin_sim = sim.lin_sim
			eskin_disim = sim.eskin_disim
			lin_disim = sim.lin_disim
			edr_sim = sim.edr_sim
			
			## new

			# Compute similarities for bad choices
			sim = similarity()
			sim.timeseries(bad_set)
			bad_timewarp = sim.edtw
			bad_euclidian = sim.euclidian_dist
			bad_euclidian_sim = sim.euclidian
			bad_cosine = sim.cosine_ent
			bad_rbf = sim.rbf
			bad_edr = sim.edr_sim

			# Compute similarties for blockwise entropy
			sim = similarity()
			sim.timeseries(ent_block)
			eb_timewarp = sim.edtw
			eb_euclidian = sim.euclidian_dist
			eb_euclidian_sim = sim.euclidian
			eb_cosine = sim.cosine_ent
			eb_rbf = sim.rbf
			eb_edr = sim.edr_sim

			# levenstein
			sim = similarity()
			leven = sim.levenstein_similarity(temp_choices)

			## new above

			# Closing trace for similarity
			print "Finished computing similarity"
			print "*************************************"

			# Compute Predictions
			no_clust = len(alpha)
			temp_unsupervised = unsupervised()

			p01 = temp_unsupervised.spectral( temp_timewarp, no_clust)
			p02 = temp_unsupervised.affinity_propagation( temp_timewarp )
			p03 = temp_unsupervised.pca_ward(temp_eucliddist,2,no_clust)
			p04 = temp_unsupervised.spectral( temp_overlap, no_clust)
			p05 = temp_unsupervised.kmeans(temp_choices,no_clust)
			p06 = temp_unsupervised.kmeans( temp_entropy, no_clust )
			p07 = temp_unsupervised.kmeans( temp_concats, no_clust )
			p08 = temp_unsupervised.spectral(cosine_cat, no_clust)
			p09 = temp_unsupervised.affinity_propagation(cosine_cat)
			p10 = temp_unsupervised.spectral(cosine_ent, no_clust)
			p11 = temp_unsupervised.affinity_propagation(cosine_ent)
			p12 = temp_unsupervised.spectral(rbf, no_clust)
			p13 = temp_unsupervised.spectral(eskin_sim, no_clust)
			p14 = temp_unsupervised.affinity_propagation(eskin_sim)
			p15 = temp_unsupervised.spectral(lin_sim, no_clust)
			p16 = temp_unsupervised.affinity_propagation(lin_sim)
			p17 = temp_unsupervised.complete_hierachical(eskin_disim,no_clust)
			p18 = temp_unsupervised.average_hierachical(eskin_disim,no_clust)
			p19 = temp_unsupervised.complete_hierachical(lin_disim,no_clust)
			p20 = temp_unsupervised.average_hierachical(lin_disim,no_clust)
			p21 = temp_unsupervised.spectral(edr_sim,no_clust)
			p22 = temp_unsupervised.affinity_propagation(edr_sim)

			# Cluster bad choices
			try:
				print 'BAD CHOICES 1'
				p23 = temp_unsupervised.spectral(bad_timewarp,no_clust)
			except:
				print 'ERROR in 1'
			
			try:	
				print 'BAD CHOICES 2'
				p24 = temp_unsupervised.affinity_propagation(bad_timewarp)
			except:
				print 'ERROR in 2'
			
			try:
				print 'BAD CHOICES 3'
				p25 = temp_unsupervised.pca_ward(bad_euclidian,2,no_clust)
			except:
				print 'ERROR in 3'
			
			try:
				print 'BAD CHOICES 4'
				p26 = temp_unsupervised.spectral(bad_euclidian_sim,no_clust)
			except:
				print 'ERROR in 4'
			
			try:
				print 'BAD CHOICES 5'
				p27 = temp_unsupervised.affinity_propagation(bad_euclidian_sim)
			except:
				print 'ERROR in 5'
			
			try:
				print 'BAD CHOICES 6'
				p28 = temp_unsupervised.spectral(bad_cosine,no_clust)
			except:
				print 'ERROR in 6'

			try:
				print 'BAD CHOICES 7'
				p29 = temp_unsupervised.affinity_propagation(bad_cosine)
			except:
				print 'ERROR in 7'
			
			try:

				print 'BAD CHOICES 8'
				p30 = temp_unsupervised.spectral(bad_rbf,no_clust)
			except:
				print 'ERROR in 8'
			
			try:
				print 'BAD CHOICES 9'
				p31 = temp_unsupervised.affinity_propagation(bad_rbf)
			except:
				print 'ERROR in 9'
			
			try:
				print 'BAD CHOICES 10'
				p32 = temp_unsupervised.spectral(bad_edr,no_clust)
			except:
				print 'ERROR in 10'

			try:
				print 'BAD CHOICES 11'
				p33 = temp_unsupervised.affinity_propagation(bad_edr)
			except:
				print 'ERROR in 11'

			try:
				print 'BAD CHOICES 12'
				p34 = temp_unsupervised.kmeans( bad_set, no_clust )
			except:
				print 'ERROR in 12'
			
			try:
				print 'BAD CHOICES 13'
				p35 = temp_unsupervised.complete_hierachical(bad_euclidian,no_clust)
			except:
				print 'ERROR in 13'
			
			try:
				print 'BAD CHOICES 14'
				p36 = temp_unsupervised.average_hierachical(bad_euclidian,no_clust)
			except:
				print 'ERROR in 14'
			
			try:
				print 'BAD CHOICES 15'
				p37 = temp_unsupervised.ward_clustering(bad_set,no_clust)
			except:
				print 'ERROR in 15'

			# Cluster blockwise entropy
			try:
				print 'BLOCKWISE 1'
				p38 = temp_unsupervised.spectral(eb_timewarp,no_clust)
			except:
				print 'ERROR in BLOCKWISE 1'	
			try:			
				print 'BLOCKWISE 2'
				p39 = temp_unsupervised.affinity_propagation(eb_timewarp)
			except:
				print 'ERROR in BLOCKWISE 2'
			try:			
				print 'BLOCKWISE 3'
				p40 = temp_unsupervised.pca_ward(eb_euclidian,2,no_clust)
			except:
				print 'ERROR in BLOCKWISE 3'				
			
			try:
				print 'BLOCKWISE 4'
				p41 = temp_unsupervised.spectral(eb_euclidian_sim,no_clust)
			except:
				print 'ERROR in BLOCKWISE 4'				
			
			try:
				print 'BLOCKWISE 5'
				p42 = temp_unsupervised.affinity_propagation(eb_euclidian_sim)
			except:
				print 'ERROR in BLOCKWISE 5'

			try:
				print 'BLOCKWISE 6'
				p43 = temp_unsupervised.spectral(eb_cosine,no_clust)
			except:
				print 'ERROR in BLOCKWISE 6'				
			
			try:
				print 'BLOCKWISE 7'
				p44 = temp_unsupervised.affinity_propagation(eb_cosine)
			except:
				print 'ERROR in BLOCKWISE 6'
			
			try:					
				print 'BLOCKWISE 8'
				p45 = temp_unsupervised.spectral(eb_rbf,no_clust)
			except:
				print 'ERROR in BLOCKWISE 8'

			try:
				print 'BLOCKWISE 9'
				p46 = temp_unsupervised.affinity_propagation(eb_rbf)
			except:
				print 'ERROR in BLOCKWISE 9'	
			
			try:
				print 'BLOCKWISE 10'
				p47 = temp_unsupervised.spectral(eb_edr,no_clust)
			except:
				print 'ERROR in BLOCKWISE 10'	

			try:
				print 'BLOCKWISE 11'
				p48 = temp_unsupervised.affinity_propagation(eb_edr)
			except:
				print 'ERROR in BLOCKWISE 11'	

			try:
				print 'BLOCKWISE 12'
				p49 = temp_unsupervised.kmeans( ent_block, no_clust )
			except:
				print 'ERROR in BLOCKWISE 12'

			try:	
				print 'BLOCKWISE 13'
				p50 = temp_unsupervised.complete_hierachical(eb_euclidian,no_clust)
			except:
				print 'ERROR in BLOCKWISE 13'	
			
			try:
				print 'BLOCKWISE 14'
				p51 = temp_unsupervised.average_hierachical(eb_euclidian,no_clust)
			except:
				print 'ERROR in BLOCKWISE 14'

			try:
				print 'BLOCKWISE 15'
				p52 = temp_unsupervised.ward_clustering(ent_block,no_clust)
			except:
				print 'ERROR in BLOCKWISE 15'	

			try:
				print 'Levenstein'
				p53 = temp_unsupervised.spectral(leven,no_clust)
			except:
				print "Error in Levenstein"	

			
			# Combine predictions for saving
			p_set = [p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,\
					p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,\
					p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,\
					p45,p46,p47,p48,p49,p50,p51,p52,p53]

			# Save names for each similarity - clustering combination
			p_names = ["spectral warp","aff prop","pca","spectral overlap",\
					"km_choice","km_ent","km_con","spect_cos_cat","aff_cos_cat",\
					"spect_cos_ent","aff_cos_ent","spect_rbf","spect_esk_sim",\
					"aff_esk_sim","spect_lin_sim","aff_lin_sim","comp_hr_esk_dis",\
					"avg_hr_esk_dis","comp_hr_lin_din","avg_hr_lin_dis",\
					"spect_edr","aff_edr", "spectral bad warp","affinity bad warp","PCA bad euclid",\
					"spectral bad eucsim","affinity bad eucsim","spectral bad cosine",\
					"affinity bad cosine", "spectral bad rbf",\
					"affinity bad rbf", "spectral bad edr", "affinity bad edr", \
					"kmeans badset","complete badset","average badset","ward badset",\
					"spectral eblock warp","affinity eblock warp","PCA eblock euclid",\
					"spectral eblock eucsim","affinity eblock eucsim","spectral eblock cosine",\
					"affinity eblock cosine", "spectral eblock rbf","affinity eblock rbf",\
					"spectral eblock edr", "affinity eblock edr","kmeans eblockset",\
					"complete eblockset","average eblockset","ward eblockset","levenstein"]

			# Compute accuracies
			acc_vector = self.full_accuracies(temp_labels,p_set)
			self.accuracy_set.append(acc_vector)

			####dom
			results=acc_vector

			for i,clster in enumerate(results):
				row = [mu, sigma, N, cluster, decision_function,alpha,tau,\
					epsilon,p_names[i],p_set[i],clster[0],clster[1],\
					clster[2],clster[3],clster[4],clster[5],clster[6],\
					0,0,0,0,0,0,0]
				dframe.loc[len(dframe)] = row
			"""
			for i,clster in enumerate(results):
				row = [mu, sigma, N, cluster, decision_function,alpha,tau,\
					epsilon,p_names[i],p_set[i],[clster[0].round(5)],[clster[1]],\
					[clster[2]],[clster[3]],[clster[4]],[clster[5]],[clster[6]],\
					0,0,0,0,0,0,0]
				dframe.loc[len(dframe)] = row
			"""
			####dom further edit
			p_len = len(p_set)
			for i in range(10,17):
				"""
				dframe.ix[:,i][step*p_len:(step+1)*p_len]=\
				zip(sum(dframe.ix[:,i][step*p_len:(step+1)*p_len],[]),dframe.ix[:,i][step*p_len:(step+1)*p_len].rank(method="min",ascending=False))
				""" # uncomment to get tupples
				dframe.ix[:,i+7][step*p_len:(step+1)*p_len]=dframe.ix[:,i][step*p_len:(step+1)*p_len].rank(method="min",ascending=False)

			####

			self.dframe = dframe

			####

			# Close trace
			print "Finished with iteration  " + str(step)
			print "*************************************"
			print "\n .\n . \n . \n"

	"""
	Auxilliary functions
	"""

	# Wrapper to compute accuracies for a set of predictions and a vector of true lables
	def full_accuracies(self,true,prediction_set):
		all_accurracies = []
		for prediction in prediction_set:
			temp_accuracies = accuracies(true,prediction)
			all_accurracies.append( temp_accuracies.full )
		return all_accurracies

	"""
	def frame(self, mu_set, sigma_set,N_set,cluster_set,seed_set,decision_function_set,alpha_set,tau_set):
		results=self.accuracy_set
		column_names=["mu","sigma","trials,","cluster","decision","alpha","tau",\
		"clustering","mis","amis","nmis","ars","complet","homogen","vmeas"]

		dframe = pd.DataFrame(columns=column_names)

		for i,desc in enumerate(results):
			for j,clster in enumerate(desc):
				row = [mu_set[i],sigma_set[i],N_set[i],cluster_set[i],\
				decision_function_set[i],alpha_set[i],tau_set[i],p_set[j],clster]
				dframe.append(row)

		self.dframe = dframe
	"""








