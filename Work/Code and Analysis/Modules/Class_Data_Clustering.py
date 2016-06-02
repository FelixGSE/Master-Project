class data_clustering:

	def prediction(self, choice_set, entropy_set,bad_set,cluster_range,labelset,save = True,path = None):

		column_names=["no_clust","algorithm", "predictions",\
		"mut inf scr","adj mis","norm mis","adj rand s","complet","homogen","vmeas",\
		"mut inf scr1","adj mis1","norm mis1","adj rand s1","complet1","homogen1","vmeas1"]

		dframe = pd.DataFrame(columns=column_names)
		
		temp_choices = choice_set
		temp_entropy = entropy_set
		temp_concats = []
		for i in range(len(choice_set)):
			temp = choice_set[i] + entropy_set[i]
			temp_concats.append(temp)
				# Compute Similarities 
				
		print "*************************************"
		print "Start computing similarity"
		print "-------------------------------------"
		sim = similarity()
		sim.timeseries(temp_entropy)	
		sim.categorical(temp_choices)
		
		print "Finished computing similarity"
		print "*************************************"
		
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

		# Reinitialize sim
		sim = similarity()
		sim.timeseries(bad_set)
		bad_timewarp = sim.edtw
		bad_euclidian = sim.euclidian_dist
		bad_euclidian_sim = sim.euclidian
		bad_cosine = sim.cosine_ent
		bad_rbf = sim.rbf
		bad_edr = sim.edr_sim

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

		counter = 1
		for itr,no_clust in enumerate(cluster_range):

			print "\n"
			print "*************************************"
			print "Started with iteration \t " + str(counter)
			print "-------------------------------------"

	
				
			# Cluster
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
			
			bad_timewarp = sim.edtw
			bad_euclidian = sim.euclidian_dist
			bad_euclidian_sim = sim.euclidian
			bad_cosine = sim.cosine_ent
			bad_rbf = sim.rbf
			bad_edr = sim.edr_sim

			p23 = temp_unsupervised.spectral(bad_timewarp,no_clust)
			p24 = temp_unsupervised.affinity_propagation(bad_timewarp)
			p25 = temp_unsupervised.pca_ward(bad_euclidian,2,no_clust)
			p26 = temp_unsupervised.spectral(bad_euclidian_sim,no_clust)
			p27 = temp_unsupervised.affinity_propagation(bad_euclidian_sim)
			p28 = temp_unsupervised.spectral(bad_cosine,no_clust)
			p29 = temp_unsupervised.affinity_propagation(bad_cosine)
			p30 = temp_unsupervised.spectral(bad_rbf,no_clust)
			p31 = temp_unsupervised.affinity_propagation(bad_rbf)
			p32 = temp_unsupervised.spectral(bad_edr,no_clust)
			p33 = temp_unsupervised.affinity_propagation(bad_edr)
			p34 = temp_unsupervised.kmeans( bad_set, no_clust )
			p35 = temp_unsupervised.complete_hierachical(bad_set,no_clust)
			p36 = temp_unsupervised.average_hierachical(bad_set,no_clust)
			p37 = temp_unsupervised.ward_clustering(bad_set,no_clust)

		

			p_set = [p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,\
					p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,\
					p30,p31,p32,p33,p34,p35,p36,p37]

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
					"kmeans badset","complete badset","average badset","ward badset"
					]

			# Compute accuracies
			acc_vector = self.full_accuracies(labelset,p_set)

			results=acc_vector
			
			for i,clster in enumerate(results):
				row = [no_clust,p_names[i],p_set[i],clster[0],clster[1],\
					clster[2],clster[3],clster[4],clster[5],clster[6],\
					0,0,0,0,0,0,0]
				dframe.loc[len(dframe)] = row

			p_len = len(p_set)
			for i in range(3,10):
				dframe.ix[:,i+7][itr*p_len:(itr+1)*p_len]=dframe.ix[:,i][itr*p_len:(itr+1)*p_len].rank(method="min")

			"""
			for i,clster in enumerate(p_set):
				row = [no_clust,p_names[i],p_set[i]]
				dframe.loc[len(dframe)] = row
			"""

			####
			print "Finished with iteration  " + str(counter)
			print "*************************************"
			print "\n .\n . \n . \n"
			counter = counter + 1

		self.dframe = dframe

	def full_accuracies(self,true,prediction_set):
		all_accurracies = []
		for prediction in prediction_set:
			temp_accuracies = accuracies(true,prediction)
			all_accurracies.append( temp_accuracies.full )
		return all_accurracies

