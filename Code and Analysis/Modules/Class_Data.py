class data:
	"""
	SET INITIAL CONDITIONS
	"""

	def __init__(self):
		self.choices = []
		self.rewards = []
		self.value_functions = []
		self.entropies = []
		self.label = []
		self.decision_function = None
		self.concat = []
		self.choices_avg = []
		self.entropies_avg = []
		self.avg_bad = []

	"""
	Create data set
	"""

	# Create data set for input parameter
	def create_data(self, individual = False, mu = [0,0], sigma = [1,1], N=10, seed=None,cluster_size=5,decision_function = "softmax", \
					alpha = [0.1,0.9],tau=[0.1,0.9],epsilon = [0.01,0.1], iowa=False, ex_data = None, no_bin = 10 ):

		# Check if input reward set is given
		if ex_data is not None:
			reward_data = ex_data

		# If not create one from class bandits
		else: 
			class_bandit = bandit(mu = mu, sigma = sigma ,N=N,seed=seed,iowa=iowa)
			reward_data = class_bandit.bandits
		
		# Determine the number of agents
		number_of_agents =  len(alpha) 

		# Define the number of agents that should be computed for each parameter setting
		cluster_range = self.cluster(cluster_size,number_of_agents)

		# Train agent on bandots and create clusters for each alpha-tau combination
		if decision_function == "softmax":

			# Save decision function
			self.decision_function = decision_function
			
			for i in range( number_of_agents ):

				# Subset parameters for generating agents
				temp_alpha = alpha[i]
				temp_tau = tau[i]
				temp_label = i
				temp_cluster_range = cluster_range[i]

				# Compute for one parameter setting a cluster of agents and choices etc.
				for j in range( temp_cluster_range ):

					# Overwrite the reward set if for each agent an individual reward set should be computed
					if individual == True:
						class_bandit = bandit(mu = mu, sigma = sigma ,N=N,seed=None,iowa=iowa)
						reward_data = class_bandit.bandits
					
					# Intialize agent and start learning
					temp_agent = agent( alpha = temp_alpha, tau = temp_tau, reward_input = reward_data,decision_function = decision_function )
					temp_agent.learn()
					
					# Save the resulting output
					self.value_functions.append( temp_agent.value_function )
					self.choices.append( temp_agent.choices )
					self.entropies.append(temp_agent.entropy)
					self.rewards.append( temp_agent.rewards )
					self.label.append(temp_label)
					self.concat.append( temp_agent.choices + temp_agent.entropy )

		# Train agent on bandots and create clusters for each alpha-tau combination
		if decision_function == "epsgreedy":
			
			# Save decision function
			self.decision_function = decision_function
			

			for i in range( number_of_agents  ):
				
				# Subset parameters for generating agents
				temp_alpha = alpha[i]
				temp_epsilon = epsilon[i]
				temp_label = i
				temp_cluster_range = cluster_range[i]
				
				# Compute for one parameter setting a cluster of agents and choices etc.
				for j in range( temp_cluster_range ):

					# Overwrite the reward set if for each agent an individual reward set should be computed
					if individual == True:
						class_bandit = bandit(mu = mu, sigma = sigma ,N=N,seed=None,iowa=iowa)
						reward_data = class_bandit.bandits
					
					# Intialize agent and start learning
					temp_agent = agent( alpha = temp_alpha, epsilon = temp_epsilon, reward_input = reward_data,decision_function = decision_function )
					temp_agent.learn()

					# Save the resulting output
					self.value_functions.append( temp_agent.value_function )
					self.choices.append( temp_agent.choices )
					self.rewards.append( temp_agent.rewards )
					self.entropies.append(temp_agent.entropy)
					self.label.append(temp_label)
					self.concat.append( temp_agent.choices + temp_agent.entropy )

		
		avg_size = N/no_bin

		for ind in self.choices:
			avg_ind=[]
			for i in range(no_bin):
				avg_ind.append(np.mean(ind[i*avg_size:(i+1)*avg_size]))
			self.choices_avg.append(avg_ind)

		for ind in self.entropies:
			avg_ind=[]
			for i in range(no_bin):
				avg_ind.append(np.mean(ind[i*avg_size:(i+1)*avg_size]))
			self.entropies_avg.append(avg_ind)

		for ind in self.choices:
			avg_ind=[]
			for i in range(no_bin):
				good = ind[i*avg_size:(i+1)*avg_size].count(mu.index(max(mu))) / float(10)
				avg_ind.append(1-good)
			self.avg_bad.append(avg_ind)


	 # Save current state of the value function, choices and experienced rewards
	def save_history( self , path = None ):

		# Define file names for storage objects for softmax decision function
		if self.decision_function == "softmax":
			# Prepare File name
			function = self.decision_function
			sys_time =  time.strftime("%H_%M_%S")
			file_type = ".txt"
			value_name = "valuefunction_" + function + "_" +  sys_time + file_type
			choice_name = "choices_" + function + "_" +  sys_time + file_type
			reward_name = "reward_" + function + "_" + sys_time + file_type
			entropy_name = "entropy_" +  function + "_" + sys_time + file_type
			label_name = "label_" + function + "_" + sys_time + file_type
		# Define file names for storage objects for epsilon greedy decision function
		if self.decision_function == "epsgreedy":
			# Prepare File name
			function = self.decision_function
			sys_time =  time.strftime("%H_%M_%S")
			file_type = ".txt"
			value_name = "valuefunction_"+ function + "_" + sys_time + file_type
			choice_name = "choices_" + function + "_" + sys_time + file_type
			reward_name = "reward_" + function + "_" + sys_time + file_type
			entropy_name = "entropy_" +  function + "_" + sys_time + file_type
			label_name = "label_" + function + "_" + sys_time + file_type
		# Combine file names and path
		if path == None:
			path = os.getcwd() + "/"
		else:
			path = path
			print path
		value_file = path + value_name
		choice_file = path + choice_name
		reward_file = path + reward_name
		entropy_file = path + entropy_name
		label_file = path + label_name

		# Save value functions, choice- and reward lists
		json.dump(self.value_functions, file(value_file, 'w'))
		json.dump(self.choices, file(choice_file, 'w'))
		json.dump(self.rewards, file(reward_file, 'w'))
		json.dump(self.entropies, file(entropy_file, 'w'))
		json.dump(self.label, file(label_file, 'w'))

	def cluster(self, item, n ):
		boolean = isinstance( item , ( int, long ) )
		if boolean == True:
			return [item] * n
		else:
			length = len(item)
			if length != n:
				raise ValueError('Cluster list has to be an integer or have the same length as number of agents')
			return item
