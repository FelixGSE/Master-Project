class bandit:
    
    """ 
    SET INITIAL CONDITIONS
    """
    
    def __init__( self, mu = [0,0] , sigma = [1,1], N = 10 , seed = None, iowa=False,\
                p1=0.5,p2=0.9,p3=0.5,p4=0.9,s1=[100,-150],s2=[100,-1150],s3=[50,0],s4=[50,-200]):
        self.mu = mu
        if iowa == False:
            self.sigma = sigma
        else:
            self.sigma = ["no","sigma"]
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
    
    def create_bandits(self, mu ,sigma, N, iowa, p1,p2,p3,p4,s1,s2,s3,s4 ):
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
                number = weighted_sample()

    
    """ 
    Auxilliary functions
    """
    
    def rnorm(self, mu, sigma, N ):
        number = np.random.normal(mu, sigma, N)
        result = number.tolist()
        return result

    # Wrapper for sampling a random number from an array with corresponding probabilities
    def weighted_sample(self, items, probability ):
        number = np.random.choice(items,1,p=probability)
        rchoice = number.tolist()[0]
        return rchoice   
