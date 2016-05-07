class bandit:
    
    """ 
    SET INITIAL CONDITIONS
    """
    
    def __init__( self, mu = [0,0] , sigma = [1,1], N = 10 , seed = None ):
        self.mu = mu
        self.sigma = sigma
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
    
    def create_bandits(self, mu ,sigma, N ):
        n_bandit = len( mu )
        bandits = []
        for i in range( n_bandit ):
            number = self.rnorm( mu[i] , sigma[i] , N )
            bandits.append(number)
        return bandits
    
    """ 
    Auxilliary functions
    """
    
    def rnorm(self, mu, sigma, N ):
        number = np.random.normal(mu, sigma, N)
        result = number.tolist()
        return result
