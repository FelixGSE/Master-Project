""" 
UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION
UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION
UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION
UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION
UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION / UNDER CONSTRUCTION
"""

class lineplot:

    def __init__( self ):
        self.plt = plt

    def 
    , color_set = None, label_set = None, xlim = None



def lineplot( x , y, color_set = None, label_set = None, xlim = None , ylim = None, \
             save = False,name = "plot" ):
    
    # Import for some reason the package insight beacuse python is blind
    import matplotlib.pyplot as plt
    
    # Define axis length
    if xlim == None:
        xmin = 0
        xmax = max( x )
        xlim = [xmin,xmax]
    if ylim == None:
        ymin = 0
        ymax = max(max(y))
        ylim = [ymin,ymax]
        
   
    # Define number of lines
    lines = len(y)
    for line in range(lines):
        print line
        temp_color = color_set[line]
        temp_label = label_set[line]
        plt.plot( x , y[line], label = temp_label , color = temp_color ) 
        
    # Define Legend position 
    plt.legend(bbox_to_anchor=(1, -0.1), ncol=3,loc=0, borderaxespad=0.)
    
    # Remove plot frame lines and axis ticks
    ax = plt.subplot(111)    
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)       
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()    
    plt.tick_params(axis = "both", which = "both", bottom = "off", top = "off",    
                    labelbottom = "on", left ="off", right = "off", labelleft = "on") 
    
    # Set x and ylim  
    plt.xlim( xlim[0],xlim[1] )
    plt.ylim( ylim[0],ylim[1] )    
    
    # Add grey lines
    for y in range(10, 91, 10):    
        plt.plot(x, [y] * len(x), "--", lw=0.5, color="black", alpha=0.3)    
      
   
    
    # Add save option
    if save == True:
        plt.savefig(name, bbox_inches = "tight")
        
    plt.show()