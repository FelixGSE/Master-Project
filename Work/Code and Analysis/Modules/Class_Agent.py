class agent:
    
    """ 
    SET INITIAL CONDITIONS
    """
    
    def __init__( self, alpha = 0.5, epsilon = 0.01, tau = 0.1 , \
        decision_function = "softmax",reward_input = None, mu = [0,0] , \
        sigma = [1,1], seed = None, init = None, time = 10, save = False ):
        
        # PARAMETERS
        self.alpha = alpha
        self.epsilon = epsilon
        self.tau = tau
        
        # DECISION FUNCTION
        self.decision_function = decision_function
        
        # BANDITS
        if reward_input == None:
            self.mu = mu
            self.sigma = sigma
            self.reward_set = None
            self.n_bandits = len( self.mu )
            self.seed = seed
        else:  
            self.reward_set = reward_input
            self.n_bandits = len( self.reward_set )
            
        # VALUE FUNCTION, REWARDS AND CHOICE LISTS
        if init == None: 
            self.value_function = self.init_value_container(self.n_bandits)
        else:
            self.value_function = self.init_value_container(self.n_bandits,self.init)
        self.choices = []
        self.rewards = []
        self.entropy = []
        
        # OTHER 
        self.time = time
        self.save = save
    
    
    """ 
    LEARNING FUNCTIONS
    """
    
    # Softmax-Decision - Returns the next choice based on boltzman distrubution
    def softmax(self, value_array, tau):
        # Check for correct input specification 
        if tau < 0.05:
            raise ValueError('Value of tau causing numerical domain error of softmax function')
        bandits = range(self.n_bandits)
        numerator = np.exp( np.array( value_array ) / float( tau ) ) 
        denominator = sum( numerator )
        boltzman_distribution = numerator / denominator
        choice = self.weighted_sample(bandits,probability = boltzman_distribution)
        return choice
    
    # Epsilon-Greedy-Decision - Returns greedy vs. random choice
    def epsilon_greedy(self, value_array, probability ):
        choice_count = len( value_array )
        explore = self.random_bool( p = probability )
        if explore == 1:
            choice = np.random.choice(choice_count)
            return choice
        else:
            optimal = value_array.index(max(value_array))
            return optimal

    """ 
    LEARNING FUNCTION
    """
    
    # Central function to run learning procedure of class agent
    def learn(self, run_time = None ):
         
        # Control run time and initilize bandits 
        if run_time == None:
            run_time = self.time
        if self.reward_set == None:
            raw = bandit( mu = self.mu, sigma = self.sigma, N = run_time, seed = self.seed )
            bandits = raw.bandits
        else:
            bandits = self.reward_set
        if  self.reward_set is not None:
            run_time = len( self.reward_set[0] )
            #print "WARNING: Note that run time was fixed to length of bandits"

        # Run learning procedure for option softmax
        if self.decision_function == "softmax":
            
            for step in range( run_time ):
                if step == 0:
                    first_descision = range(self.n_bandits)
                    current_decision = self.weighted_sample(first_descision,probability=None)
                    current_reward = bandits[current_decision][step]
                else:
                # Choose next action and reward
                    states = self.current_values_lookup( self.value_function )
                    current_decision = self.softmax( value_array = states , tau = self.tau)
                    current_reward = bandits[current_decision][step]
                
                # Update value function and store decision and rewards 
                self.choices.append( current_decision )
                self.rewards.append( current_reward )
                self.update_value_functions( current_decision, current_reward, self.alpha  )

                # Compute and update entropy
                current_entropy = self.shannons_entropy( self.choices, self.n_bandits )
                self.entropy.append( current_entropy )

        # Run learning procedure for option epsilon greedy 
        if self.decision_function == "epsgreedy":
         
            for step in range( run_time ):
                if step == 0:
                    first_descision = range(self.n_bandits)
                    current_decision = self.weighted_sample(first_descision,probability=None)
                    current_reward = bandits[current_decision][step]
                else:
                    # Choose next action and reward
                    states = self.current_values_lookup(self.value_function)
                    current_decision = self.epsilon_greedy( value_array = states , probability = self.epsilon)
                    current_reward = bandits[current_decision][step]
     
                # Update value function and store decision and rewards 
                self.choices.append( current_decision )
                self.rewards.append( current_reward )
                self.update_value_functions( current_decision, current_reward, self.alpha  )

                # Compute and update entropy 
                current_entropy = self.shannons_entropy( self.choices, self.n_bandits )
                self.entropy.append( current_entropy )
 
    """ 
    AUXILLIARY FUNCTIONS
    """

    # Compute the entropy based on current choice probabilities
    def shannons_entropy(self,choice_vector,nchoices):
		unique_values = range(nchoices)
		frequencies = [choice_vector.count(value) for value in unique_values]
		total_counts = float(sum(frequencies))
		probabilities = [x / float(total_counts) for x in frequencies]
		entropy_vector = []
		for probability in probabilities:
			try:
				temp_value = probability * math.log(probability,2)
				entropy_vector.append(temp_value)
			except:
				temp_value = 0
				entropy_vector.append(temp_value)
		entropy = -sum( entropy_vector )
		return entropy

    # Wrapper function for sampling randomly TRUE or FALSE with probability p
    def random_bool(self, p = 0.1 ):
        number = np.random.binomial( 1 , p, 1 )
        result = number.tolist()[0] 
        return result

    # Wrapper for sampling a random number from an array with corresponding probabilities
    def weighted_sample(self, items, probability ):
        number = np.random.choice(items,1,p=probability)
        rchoice = number.tolist()[0]
        return rchoice   
    
    # Inititialize n value storages 0 or specified initial values
    def init_value_container(self, vfcount , init_val = None ):
        max_itter = vfcount
        value_functions = []
        if init_val == None:
            init_val = [0] * max_itter
        for i in range( max_itter ):
            temp_val = init_val[i]
            temp_list = [temp_val]
            value_functions.append(temp_list)
        return value_functions

    # Wrapper for looking up the last value in each value_function ( == last column of list of list )
    def current_values_lookup(self, listoflist ):
        cols = len(listoflist[0]) - 1
        last_value = [row[cols] for row in listoflist]
        return last_value
    
    # Update value functions according to choices rewards and alpha
    def update_value_functions(self, choice, reward, alpha ):
        for i in range(  self.n_bandits  ):
            current_value_function = self.value_function[i]
            old_value = current_value_function[-1]
            if i == choice:
                new_value = old_value + alpha * ( reward - old_value )
            else:
                new_value = old_value
            
            current_value_function.append(new_value)
        
    """ 
    BACK UP AND RESET
    """
        
    # Save current state of the value function, choices and experienced rewards                  
    def save_history( self , path = None ):
        
        # Define file names for storage objects for softmax decision function
        if self.decision_function == "softmax":
            str_alpha = "alpha_" + str(self.alpha)
            str_tau = "_tau_" + str(self.tau)
            file_type = ".txt"
            sufix = str_alpha + str_tau + file_type
            value_name = "valuefunction_" + sufix
            choice_name = "choices" + sufix
            reward_name = "reward" + sufix
            entropy_name = "entropy" + sufix
        
        # Define file names for storage objects for epsilon greedy decision function 
        if self.decision_function == "epsgreedy":
            # Prepare File name - Parameters
            str_alpha = "alpha_" + str(self.alpha)
            str_epsilon = "_epsilon_" + str(self.epsilon)
            file_type = ".txt"
            sufix = str_alpha + str_epsilon + file_type
            value_name = "valuefunction_" + sufix
            choice_name = "choices" + sufix
            reward_name = "reward" + sufix
            entropy_name = "entropy" + sufix

        # Combine file names and path
        if path == None:
            path = os.getcwd() + "/"
        value_file = path + value_name
        choice_file = path + choice_name
        reward_file = path + reward_name
        entropy_file = path + entropy_name

        # Save value functions, choice- and reward lists
        json.dump(self.value_function, file(value_file, 'w'))
        json.dump(self.choices, file(choice_file, 'w'))
        json.dump(self.rewards, file(reward_file, 'w'))
        json.dump(self.entropy, file(entropy_file, 'w'))
    
    # Clear value function of the agent      
    def re_init( self, init = None ):
        if init == None: 
            self.value_function = self.init_value_container(self.n_bandits)
        else:
            self.value_function = self.init_value_container(self.n_bandits,self.init)
        self.choices = []
        self.rewards = []