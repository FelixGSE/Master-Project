class bandit:
    
    """ 
    SET INITIAL CONDITIONS
    """
    
    def __init__( self, mu = [0,0] , sigma = [1,1], N = 10 , seed = None, iowa=False,prob=[[0.5,0.5],[0.9,0.1],[0.5,0.5],[0.9,0.1]],deck=[[100,-150],[100,-1150],[50,0],[50,-200]]):
        self.mu = mu
        self.prob = prob
        self.deck = deck
        self.iowa = iowa
        self.N = N
        if iowa == False:
            self.sigma = sigma
        else:
            self.sigma = ["no","sigma"]
            self.bandits = self.create_bandits(mu=self.mu,sigma=self.sigma,N=self.N,iowa=iowa,probability=self.prob,deck=self.deck)
        self.seed = seed
        if self.seed == None:
            self.bandits = self.create_bandits(mu=self.mu,sigma=self.sigma,N=self.N,iowa=iowa,probability=self.prob,deck=self.deck)
        else:
            np.random.seed( self.seed )
            self.bandits = self.create_bandits(mu=self.mu,sigma=self.sigma,N=self.N,iowa=iowa,probability=self.prob,deck=self.deck)
    
    """ 
    Function to create bandits
    """
    
    # Create Bandits with input arguments 
    def create_bandits(self, mu ,sigma, N, iowa, probability, deck ):
        
        # Compute bandits from normal distribution
        if iowa == False:

            # Define the number of bandits to create
            n_bandit = len( mu )
            # Initialize storage list
            bandits = []

            for i in range( n_bandit ):

                # Compute a vector of N normally distributed numbers with mu and sigma
                number = self.rnorm( mu[i] , sigma[i] , N )
                # Append vector to bandits
                bandits.append(number)

            return bandits

        # Simmulate bandits like IOWA test
        else:
            n_bandit = 4
            bandits = []
            for i in range(n_bandit):
                number = self.weighted_iowa(deck[i],times=N,probability=probability[i])
                bandits.append(number)
            return bandits

    
    """ 
    Auxilliary functions
    """
    
    # Wrapper to compute a vector with N normally distributed numbers
    def rnorm(self, mu, sigma, N ):
        number = np.random.normal(mu, sigma, N)
        result = number.tolist()
        return result

    # Wrapper for sampling a random number from an array with corresponding probabilities
    def weighted_sample(self, items, probability ):
        number = np.random.choice(items,1,p=probability)
        rchoice = number.tolist()[0]
        return rchoice   

    # Sample items from a list with probility distribution
    def weighted_iowa(self, items, times, probability ):
        number = np.random.choice(items,times,p=probability)
        rchoice = number.tolist()
        return rchoice  


