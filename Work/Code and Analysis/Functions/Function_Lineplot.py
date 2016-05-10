# Import some necessary packages
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math 

# Define lineplot function
def lineplot( x , y, color_set = None, label_set = None, xlim = None , ylim = None, \
             legend = False, horizontal_grid = True, save = False, name = "my_line_plot" ):

    # Define number of lines
    lines = len(y)
    # Define color set
    if color_set == None:
        color_set = sns.diverging_palette(220, 20, n=lines)

    # Add lines to plot
    for line in range(lines):
        temp_color = color_set[line]
        if label_set == None:
            plt.plot( x , y[line], color = temp_color ) 
        else:
            temp_label = label_set[line]
            plt.plot( x , y[line], label = temp_label , color = temp_color ) 
        
    # Define Legend position
    if legend == True:
        plt.legend(bbox_to_anchor=(1, -0.1), ncol=3,loc=0, borderaxespad=0.)
    
    # Remove plot frame lines and axis ticks
    ax = plt.subplot(111)   
    ax.set_axis_bgcolor('white') 
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)       
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()    
    plt.tick_params(axis = "both", which = "both", bottom = "off", top = "off",    
                    labelbottom = "on", left ="off", right = "off", labelleft = "on") 
    
    # Define axis length
    if xlim == None:
        xmin = 0
        xmax = max( x )
        xlim = [xmin,xmax]
    if ylim == None:
        temp_list = [item for sublist in y for item in sublist]
        ymin = min(temp_list)
        ymax = max(temp_list)
        ylim = [ymin,ymax]
        print ylim
    # Set x and ylim  
    adjustment = ( ylim[1] - ylim[0] ) / 10.
    plt.xlim( xlim[0],xlim[1] )
    plt.ylim( ylim[0] - adjustment ,ylim[1] + adjustment)    
    
    # Add grey lines
    if horizontal_grid == True:
        difference = ( ylim[1] - ylim[0] ) / 10.
        #lower_range = int( math.ceil( ylim[0] / 10.) * 10 )
        #print lower_range 
        #upper_range = int( math.floor( ylim[1] / 10.) * 10 )

        #print upper_range
        iter_range = np.arange(ylim[0],ylim[1],difference)
        #iter_range = range( int(ylim[0]), int( ylim[1]), int(difference )) 
        for y in iter_range:    
            plt.plot(x, [y] * len(x), "--", lw=0.5, color="black", alpha=0.3)    
      
    
    # Add save option
    if save == True:
        plt.savefig(name, bbox_inches = "tight")

    return plt.show()


# TEST
import os 
import json

path_data = "/Users/felix/Documents/GSE/Term 3/Master_Project/Master-Project/Work/Code and Analysis/Artificial Data Sets/d01/"
os.chdir(path_data)  

# Load Data
with open('valuefunction_softmax_19_32_31.txt') as data_file:    
    data = json.load(data_file)


sub=data[0]
x = range(len(sub[0]))

lineplot(x,sub)





