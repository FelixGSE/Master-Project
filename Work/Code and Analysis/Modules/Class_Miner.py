class miner:

	def __init__(self):

		self.accuracy_set = []


	def prediction(self, mu_set, sigma_set,N_set,cluster_set,seed_set,decision_function_set,alpha_set,tau_set,epsilon_set = None, iowa = False):

		runtime = range(len(mu_set))

		column_names=["mu","sigma","trials","cluster size","decision","alpha","tau","epsilon",\
			"clustering","labels","mut inf scr","adj mis","norm mis","adj rand s","complet","homogen","vmeas",\
			"mut inf scr1","adj mis1","norm mis1","adj rand s1","complet1","homogen1","vmeas1"]

		column_names_1=["mut inf scr","adj mis","norm mis","adj rand s","complet","homogen","vmeas"]

		dframe = pd.DataFrame(columns=column_names)
		dframe1 = pd.DataFrame(columns=column_names_1)

		for step in runtime:

			# Print trace
			print "\n"
			print "*************************************"
			print "Started with iteration \t " + str(step)
			print "-------------------------------------"

			# Subset data 
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

			# Create data 
			temp_data = data()
			temp_data.create_data( individual = True, mu = mu, sigma = sigma, N = N,
							cluster_size = cluster, seed = seed, decision_function = decision_function, 
							alpha = alpha, tau = tau, epsilon =  epsilon, iowa=iowa)
			print temp_data.rewards		
			# Extract features
			temp_entropy = temp_data.entropies
			temp_choices = temp_data.choices 
			temp_labels  = temp_data.label
			temp_concats = temp_data.concat 

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
			

			p_set = [p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,\
					p15,p16,p17,p18,p19,p20,p21,p22]
			p_names = ["spectral warp","aff prop","pca","spectral overlap",\
					"km_choice","km_ent","km_con","spect_cos_cat","aff_cos_cat",\
					"spect_cos_ent","aff_cos_ent","spect_rbf","spect_esk_sim",\
					"aff_esk_sim","spect_lin_sim","aff_lin_sim","comp_hr_esk_dis",\
					"avg_hr_esk_dis","comp_hr_lin_din","avg_hr_lin_dis",\
					"spect_edr","aff_edr"]

			# Compute accuracies
			acc_vector = self.full_accuracies(temp_labels,p_set)
			self.accuracy_set.append(acc_vector)

			####dom
			results=acc_vector
			

			for i,clster in enumerate(results):
				row = [mu, sigma, N, cluster, decision_function,alpha,tau,\
					epsilon,p_names[i],p_set[i],[clster[0].round(5)],[clster[1]],\
					[clster[2]],[clster[3]],[clster[4]],[clster[5]],[clster[6]],\
					0,0,0,0,0,0,0]
				dframe.loc[len(dframe)] = row

			####dom further edit
			p_len = len(p_set)
			for i in range(10,17):
				dframe.ix[:,i][step*p_len:(step+1)*p_len]=\
				zip(sum(dframe.ix[:,i][step*p_len:(step+1)*p_len],[]),dframe.ix[:,i][step*p_len:(step+1)*p_len].rank(method="min"))
				dframe.ix[:,i+7][step*p_len:(step+1)*p_len]=dframe.ix[:,i][step*p_len:(step+1)*p_len].rank(method="min")

			####

			self.dframe = dframe

			####


			print "Finished with iteration  " + str(step)
			print "*************************************"
			print "\n .\n . \n . \n"

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








