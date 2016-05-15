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

	"""
	Create data set
	"""

	def create_data(self, mu = [0,0], sigma = [1,1], N=10, seed=None,cluster_size=5,decision_function = "softmax", alpha = [0.1,0.9],tau=[0.1,0.9],epsilon = [0.01,0.1] ):

		# Create data from class bandit
		class_bandit = bandit(mu = mu, sigma = sigma ,N=N,seed=seed)
		reward_data = class_bandit.bandits

		# Train agent on bandots and create clusters for each alpha-tau combination
		if decision_function == "softmax":
			self.decision_function = decision_function
			for i in range( len(alpha) ):
				temp_alpha = alpha[i]
				temp_tau = tau[i]
				temp_label = i
				for j in range( cluster_size ):
					temp_agent = agent( alpha = temp_alpha, tau = temp_tau, reward_input = reward_data,decision_function = decision_function )
					temp_agent.learn()
					self.value_functions.append( temp_agent.value_function )
					self.choices.append( temp_agent.choices )
					self.entropies.append(temp_agent.entropy)
					self.rewards.append( temp_agent.rewards )
					self.label.append(temp_label)
		# Train agent on bandots and create clusters for each alpha-tau combination
		if decision_function == "epsgreedy":
			self.decision_function = decision_function
			for i in range( len(alpha) ):
				temp_alpha = alpha[i]
				temp_epsilon = epsilon[i]
				temp_label = i
				for j in range( cluster_size ):
					temp_agent = agent( alpha = temp_alpha, epsilon = temp_epsilon, reward_input = reward_data,decision_function = decision_function )
					temp_agent.learn()
					self.value_functions.append( temp_agent.value_function )
					self.choices.append( temp_agent.choices )
					self.rewards.append( temp_agent.rewards )
					self.entropies.append(temp_agent.entropy)
					self.label.append(temp_label)
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
		json.dump(self.rewards, file(entropy_file, 'w'))
		json.dump(self.label, file(label_file, 'w'))
