class miner:

	def __init__(self):

		self.accuracy_set = []


	def prediction(self, mu_set, sigma_set,N_set,cluster_set,seed_set,decision_function_set,alpha_set,tau_set,epsilon_set = None):

		runtime = range(len(mu_set))

		column_names=["mu","sigma","trials","cluster","decision","alpha","tau",\
			"clustering","labels","mut inf scr","adj mis","norm mis","adj rand s","complet","homogen","vmeas"]

		dframe = pd.DataFrame(columns=column_names)

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
			tau = tau_set[step]
			if epsilon_set == None:
				epsilon = None
			else:
				epsilon = epsilon_set[step]

			# Create data 
			temp_data = data()
			temp_data.create_data( individual = True, mu = mu, sigma = sigma, N = N,
							cluster_size = cluster, seed = seed, decision_function = decision_function, 
							alpha = alpha, tau = tau, epsilon =  epsilon)
			
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
			
			# Compute Predictions
			no_clust = len(alpha)
			temp_unsupervised = unsupervised()

			p01 = temp_unsupervised.spectral( temp_timewarp, no_clust)
			p02 = temp_unsupervised.affinity_propagation( temp_timewarp )
			p03 = temp_unsupervised.pca_ward(temp_eucliddist,2,no_clust)
			p04 = temp_unsupervised.kmeans(temp_choices,no_clust)
			p05 = temp_unsupervised.spectral( temp_overlap, no_clust)
			p06 = temp_unsupervised.kmeans( temp_concats, no_clust )
			p07 = temp_unsupervised.kmeans( temp_entropy, no_clust )

			p_set = [p01,p02,p03,p04,p05,p06,p07]
			p_names = ["spectral warp","aff prop","pca","km_choice","spectral overlap",\
					"km_con","km_ent"]

			# Compute accuracies
			acc_vector = self.full_accuracies(temp_labels,p_set)
			self.accuracy_set.append(acc_vector)

			####dom
			results=acc_vector
			

			for i,clster in enumerate(results):
				row = [mu_set[step],sigma_set[step],N_set[step],cluster_set[step],\
				decision_function_set[step],alpha_set[step],tau_set[step],p_names[i],p_set[i],\
				clster[0],clster[1],clster[2],clster[3],clster[4],clster[5],clster[6]]
				dframe.loc[len(dframe)] = row

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








