class data:
    """
    SET INITIAL CONDITIONS
    """
    
    def __init__(self):
        self.choices = []
        self.rewards = []
        self.value_functions = []

  	"""
    Create data set
    """

    def create_data(self, mu = [0,0], sigma = [1,1], N=10, seed=None,cluster=5,decision_function = "softmax", alpha = [0.1,0.9],tau=[0.1,0.9],epsilon = [0.01,0.1] ):
        class_bandit = bandit(mu = mu, sigma = sigma ,N=N,seed=seed)
        reward_data = class_bandit.bandits
        nclust = cluster 

        if decision_function == "softmax":
        	for i in range( len(alpha) ):
				temp_alpha = alpha[i]
				temp_tau = tau[i]
				for j in range( cluster ):
					temp_agent = agent( alpha = temp_alpha, tau = temp_tau, reward_input = reward_data,decision_function = decision_function )
					temp_agent.learn()
					self.value_functions.append( temp_agent.value_function )
					self.choices.append( temp_agent.choices )
					self.rewards.append( temp_agent.rewards )
		if decision_function == "epsgreedy":
			for i in range( len(alpha) ):
				temp_alpha = alpha[i]
				temp_epsilon = epsilon[i]
				for j in range( cluster ):
					temp_agent = agent( alpha = temp_alpha, epsilon = temp_epsilon, reward_input = reward_data,decision_function = decision_function )
					temp_agent.learn()
					self.value_functions.append( temp_agent.value_function )
					self.choices.append( temp_agent.choices )
					self.rewards.append( temp_agent.rewards )