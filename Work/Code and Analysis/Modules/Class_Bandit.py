class bandit:
    
    """ 
    SET INITIAL CONDITIONS
    """
    
    def __init__( self, mu = [0,0] , sigma = [1,1], N = 10 , seed = None, iowa=False,\
                prob=[[0.5,0.5],[0.9,0.1],[0.5,0.5],[0.9,0.1]],\
                decl=[[100,-150],[100,-1150],[50,0],[50,-200]]):
        self.mu = mu
        self.prob = prob
        self.deck = deck
        if iowa == False:
            self.sigma = sigma
        else:
            self.sigma = ["no","sigma"]
            self.bandits = create_bandits()
        self.N = N
        self.seed = seed
        if self.seed == None:
            self.bandits = self.create_bandits(self.mu,self.sigma,self.N)
        else:
            np.random.seed( self.seed )
            self.bandits = self.create_bandits(self.mu,self.sigma,self.N)
    
    """ 
    Function to create bandits
    """
    
    def create_bandits(self, mu ,sigma, N, iowa, prob,deck ):
        if iowa == False:
            n_bandit = len( mu )
            bandits = []
            for i in range( n_bandit ):
                number = self.rnorm( mu[i] , sigma[i] , N )
                bandits.append(number)
            return bandits
        else:
            n_bandit = 4
            bandits = []
            for i in range(n_bandit):
                number = self.weighted_sample(deck[i],N,p=prob[i])
                bandits.append(number)
            return bandits

    
    """ 
    Auxilliary functions
    """
    
    def rnorm(self, mu, sigma, N ):
        number = np.random.normal(mu, sigma, N)
        result = number.tolist()
        return result

    # Wrapper for sampling a random number from an array with corresponding probabilities
    def weighted_sample(self, items, times, probability ):
        number = np.random.choice(items,times,p=probability)
        rchoice = number.tolist()[0]
        return rchoice   
