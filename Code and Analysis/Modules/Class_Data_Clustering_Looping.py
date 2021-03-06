class data_clustering_looping:

	def prediction(self, choice_set, entropy_set,bad_set,ent_block,cluster_range,labelset,save = True,path = None):

		# Set column names for final data frame 
		"""
		column_names=["no_clust","algorithm", "predictions",\
		"mut inf scr","adj mis","norm mis","adj rand s","complet","homogen","vmeas",\
		"mut inf scr1","adj mis1","norm mis1","adj rand s1","complet1","homogen1","vmeas1"]
		"""

		# Intialize final data frame as storage object
		#dframe = pd.DataFrame(columns=column_names)
		
		# Init variables for prediction procedure
		temp_choices = choice_set
		temp_entropy = entropy_set
		temp_concats = []
		aux = auxilliary()
		temp_bad_cum = aux.avg_bad_cum(choice_set)

		# Compute a concatenated vector
		for i in range(len(choice_set)):
			temp = choice_set[i] + entropy_set[i]
			temp_concats.append(temp)
		
		# Compute Similarities - Begin Trace	
		print "*************************************"
		print "Start computing similarity"
		print "-------------------------------------"
		sim = similarity()
		sim.timeseries(temp_entropy)
		sim.categorical(temp_choices)

		# Subset result similarities
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

		# Compute similarities for bad choices
		sim = similarity()
		sim.timeseries(bad_set)
		bad_timewarp = sim.edtw
		bad_euclidian = sim.euclidian_dist
		bad_euclidian_sim = sim.euclidian
		bad_cosine = sim.cosine_ent
		bad_rbf = sim.rbf
		bad_edr = sim.edr_sim

		# Compute similarities for blockwise entropy
		sim = similarity()
		sim.timeseries(ent_block)
		eb_timewarp = sim.edtw
		eb_euclidian = sim.euclidian_dist
		eb_euclidian_sim = sim.euclidian
		eb_cosine = sim.cosine_ent
		eb_rbf = sim.rbf
		eb_edr = sim.edr_sim

		# Compute similarities 
		sim = similarity()
		sim.timeseries(temp_bad_cum)
		b_cum_timewarp = sim.edtw
		b_cum_euclidian = sim.euclidian_dist
		b_cum_euclidian_sim = sim.euclidian
		b_cum_cosine = sim.cosine_ent
		b_cum_rbf = sim.rbf
		b_cum_edr = sim.edr_sim

		# levenstein
		sim = similarity()
		leven = sim.levenstein_similarity(temp_choices)
		
		# Closing trace for similarity
		print "Finished computing similarity"
		print "*************************************"
		
		# Save similarities for ploting etc.
		if save == True:
			
			if path == None:
				path = os.getcwd() + "/"
			else:
				path = path
			file_type = ".txt"

			edtw_name = path + 'timewarp' + file_type
			eucliddist_name =  path + 'eucliddist' + file_type
			overlap_name = path + 'overlap' + file_type 
			cosine_cat_name = path + 'cosine_cat' + file_type 
			cosine_ent_name = path + 'cosine_ent' + file_type 
			rbf_name = path + 'rbf' + file_type 
			eskin_sim_name = path + 'eskin_sim' + file_type
			lin_sim_name = path + 'lin_sim' + file_type
			eskin_disim_name = path + 'eskin_disim_name' + file_type
			lin_disim_name = path + 'lin_disim' +  file_type
			edr_sim_name = path + 'edr_sim' + file_type 
			bad_timewarp_name = path + 'bad_timewarp' + file_type
			bad_euclidian_name =  path + 'bad_euclidian' + file_type
			bad_euclidian_sim_name = path + 'bad_euclidian_sim' + file_type
			bad_cosine_name  =path + 'bad_cosine' + file_type
			bad_rbf_name = path + 'bad_rbf' + file_type
			bad_edr_name = path + 'bad_edr' + file_type

			b_cum_timewarp_name = path + 'b_cum_timewarp' + file_type
			b_cum_euclidian_name =  path + 'b_cum_euclidian' + file_type
			b_cum_euclidian_sim_name = path + 'b_cum_euclidian_sim' + file_type
			b_cum_cosine_name  =path + 'b_cum_cosine' + file_type
			b_cum_rbf_name = path + 'b_cum_rbf' + file_type
			b_cum_edr_name = path + 'b_cum_edr' + file_type


 			json.dump(temp_timewarp.tolist(), file(edtw_name, 'w'))
			json.dump(temp_eucliddist.tolist(), file(eucliddist_name, 'w'))
			json.dump(temp_overlap.tolist(), file(overlap_name, 'w'))
			json.dump(cosine_cat.tolist(), file(cosine_cat_name, 'w'))
			json.dump(cosine_ent.tolist(), file(cosine_ent_name, 'w'))
			json.dump(rbf.tolist(), file(rbf_name, 'w'))
			json.dump(eskin_sim.tolist(), file(eskin_sim_name, 'w'))
			json.dump(lin_sim.tolist(), file(lin_sim_name, 'w'))
			json.dump(eskin_disim.tolist(), file(eskin_disim_name, 'w'))
			json.dump(lin_disim.tolist(), file(lin_disim_name, 'w'))
			json.dump(edr_sim.tolist() , file(edr_sim_name, 'w'))

			json.dump(bad_timewarp.tolist(), file(bad_timewarp_name, 'w'))
			json.dump(bad_euclidian.tolist(), file(bad_euclidian_name, 'w'))
			json.dump(bad_euclidian_sim.tolist(), file(bad_euclidian_sim_name, 'w'))
			json.dump(bad_cosine.tolist(), file(bad_cosine_name, 'w'))
			json.dump(bad_rbf.tolist(), file(bad_rbf_name, 'w'))
			json.dump(bad_edr.tolist() , file(bad_edr_name, 'w'))

			json.dump(b_cum_timewarp.tolist(), file(b_cum_timewarp_name, 'w'))
			json.dump(b_cum_euclidian.tolist(), file(b_cum_euclidian_name, 'w'))
			json.dump(b_cum_euclidian_sim.tolist(), file(b_cum_euclidian_sim_name, 'w'))
			json.dump(b_cum_cosine.tolist(), file(b_cum_cosine_name, 'w'))
			json.dump(b_cum_rbf.tolist(), file(b_cum_rbf_name, 'w'))
			json.dump(b_cum_edr.tolist() , file(b_cum_edr_name, 'w'))

		# Set counter for trace
		counter = 1

		no_clust = 2
		frame_list = []
		# Run clustering
		for itr in range(20):

			column_names=["no_clust","algorithm", "predictions",\
			"mut inf scr","adj mis","norm mis","adj rand s","complet","homogen","vmeas"]

			dframe = pd.DataFrame(columns=column_names)

			# Open Trace for clustering
			print "\n"
			print "*************************************"
			print "Started with iteration \t " + str(counter)
			print "-------------------------------------"

			# Cluster entropy, choices and concat
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

			# Cluster bad cumulative choices
			try:
				print 'BAD CHOICES 1'
				p53 = temp_unsupervised.spectral(b_cum_timewarp,no_clust)
			except:
				print 'ERROR in 1'
			
			try:	
				print 'BAD CHOICES 2'
				p54 = temp_unsupervised.affinity_propagation(b_cum_timewarp)
			except:
				print 'ERROR in 2'
			
			try:
				print 'BAD CHOICES 3'
				p55 = temp_unsupervised.pca_ward(b_cum_euclidian,2,no_clust)
			except:
				print 'ERROR in 3'
			
			try:
				print 'BAD CHOICES 4'
				p56 = temp_unsupervised.spectral(b_cum_euclidian_sim,no_clust)
			except:
				print 'ERROR in 4'
			
			try:
				print 'BAD CHOICES 5'
				p57 = temp_unsupervised.affinity_propagation(b_cum_euclidian_sim)
			except:
				print 'ERROR in 5'
			
			try:
				print 'BAD CHOICES 6'
				p58 = temp_unsupervised.spectral(b_cum_cosine,no_clust)
			except:
				print 'ERROR in 6'

			try:
				print 'BAD CHOICES 7'
				p59 = temp_unsupervised.affinity_propagation(b_cum_cosine)
			except:
				print 'ERROR in 7'
			
			try:
				print 'BAD CHOICES 8'
				p60 = temp_unsupervised.spectral(b_cum_rbf,no_clust)
			except:
				print 'ERROR in 8'
			
			try:
				print 'BAD CHOICES 9'
				p61 = temp_unsupervised.affinity_propagation(b_cum_rbf)
			except:
				print 'ERROR in 9'
			
			try:
				print 'BAD CHOICES 10'
				p62 = temp_unsupervised.spectral(b_cum_edr,no_clust)
			except:
				print 'ERROR in 10'

			try:
				print 'BAD CHOICES 11'
				p63 = temp_unsupervised.affinity_propagation(b_cum_edr)
			except:
				print 'ERROR in 11'

			try:
				print 'BAD CHOICES 12' # has to be on initial set
				p64 = temp_unsupervised.kmeans( temp_bad_cum, no_clust )
			except:
				print 'ERROR in 12'
			
			try:
				print 'BAD CHOICES 13'
				p65 = temp_unsupervised.complete_hierachical(b_cum_euclidian,no_clust)
			except:
				print 'ERROR in 13'
			
			try:
				print 'BAD CHOICES 14'
				p66 = temp_unsupervised.average_hierachical(b_cum_euclidian,no_clust)
			except:
				print 'ERROR in 14'
			
			try:
				print 'BAD CHOICES 15' # also has to be on initial set
				p67 = temp_unsupervised.ward_clustering(temp_bad_cum,no_clust)
			except:
				print 'ERROR in 15'

			try:
				print "Levenstein"
				p68 = temp_unsupervised.spectral(leven,no_clust)
			except:
				print "Error in Levenstein"
		

			# combine predictions for output
			p_set = [p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,\
					p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,\
					p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,\
					p45,p46,p47,p48,p49,p50,p51,p52,p53,p54,p55,p56,p57,p58,p59,\
					p60,p61,p62,p63,p64,p65,p66,p67,p68]

			# Set names for similarity - clustering combination
			p_names = [
					"spectral warp","aff prop","pca","spectral overlap",\
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
					"affinity eblock cosine", "spectral eblock rbf",\
					"affinity eblock rbf", "spectral eblock edr", "affinity eblock edr", \
					"kmeans eblockset","complete eblockset","average eblockset","ward eblockset",\
					"spectral b_cum warp","affinity b_cum warp","PCA b_cum euclid",\
					"spectral b_cum eucsim","affinity b_cum eucsim","spectral b_cum cosine",\
					"affinity b_cum cosine", "spectral b_cum rbf",\
					"affinity b_cum rbf", "spectral b_cum edr", "affinity b_cum edr", \
					"kmeans badcumset","complete badcumset","average badcumset","ward badcumset",\
					"levenstein"
					]

			# Compute accuracies
			acc_vector = self.full_accuracies(labelset,p_set)

			results=acc_vector
			
			"""
			for i,clster in enumerate(results):
				row = [no_clust,p_names[i],p_set[i],clster[0],clster[1],\
					clster[2],clster[3],clster[4],clster[5],clster[6],\
					0,0,0,0,0,0,0]
				dframe.loc[len(dframe)] = row
			"""

			for i,clster in enumerate(results):
				row = [no_clust,p_names[i],p_set[i],clster[0],clster[1],\
					clster[2],clster[3],clster[4],clster[5],clster[6]]
				dframe.loc[len(dframe)] = row

			"""
			p_len = len(p_set)
			for i in range(3,10):
				dframe.ix[:,i+7][itr*p_len:(itr+1)*p_len]=dframe.ix[:,i][itr*p_len:(itr+1)*p_len].rank(method="min",ascending=False)
			"""

			"""
			for i,clster in enumerate(p_set):
				row = [no_clust,p_names[i],p_set[i]]
				dframe.loc[len(dframe)] = row
			"""

			frame_list.append(dframe)

			# Closing trace for clustering 
			print "Finished with iteration  " + str(counter)
			print "*************************************"
			print "\n .\n . \n . \n"

			# Update counter for trace
			counter = counter + 1

		# Save data frame
		#self.dframe = dframe
		self.dframe = frame_list
		cols = ['mut inf scr', 'adj mis','norm mis', 'adj rand s', 'complet', 'homogen', 'vmeas']
		sub01 = frame_list[0].ix[:,:2]
		sub02 = aux.statistics_df(frame_list,cols)
		avg_frame = pd.concat([sub01,sub02],axis=1)
		self.avg_frame = avg_frame

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

