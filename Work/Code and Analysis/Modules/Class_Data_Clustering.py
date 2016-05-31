class data_clustering:

	def prediction(self, choice_set, entropy_set,cluster_range,save = True,path = None):

		column_names=["no_clust","algorithm", "predictions"]

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

		counter = 1
		for no_clust in cluster_range:

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
			

			p_set = [p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,\
					p15,p16,p17,p18,p19,p20,p21,p22]

			p_names = [
					"spectral warp","aff prop","pca","spectral overlap",\
					"km_choice","km_ent","km_con","spect_cos_cat","aff_cos_cat",\
					"spect_cos_ent","aff_cos_ent","spect_rbf","spect_esk_sim",\
					"aff_esk_sim","spect_lin_sim","aff_lin_sim","comp_hr_esk_dis",\
					"avg_hr_esk_dis","comp_hr_lin_din","avg_hr_lin_dis",\
					"spect_edr","aff_edr"
					]

			for i,clster in enumerate(p_set):
				row = [no_clust,p_names[i],p_set[i]]
				dframe.loc[len(dframe)] = row
			
			####
			print "Finished with iteration  " + str(counter)
			print "*************************************"
			print "\n .\n . \n . \n"
			counter = counter + 1

		self.dframe = dframe



