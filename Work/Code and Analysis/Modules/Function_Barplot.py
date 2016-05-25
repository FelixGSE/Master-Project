import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math 

def barplot(data, width = 0.2, off = 0.5,color_set = None,xlab = None, ylab = None,main = None):
    fig, ax = plt.subplots()
    nbars = len(data)
    try:
        nprob = len(data[0])
    except:
        nprob = nbars
        data = [data]
    ind = np.arange(nbars) + 0.
    width = width
    # Define x- and ylim
    plt.ylim(0,1)
    #xmin = ind[0] - off
    #xmax = ind[-1] + off
    #plt.xlim(xmin,xmax)

    # Define Color set
    if color_set == None:
        color_set = sns.diverging_palette(220, 20, n=nbars)
    # Add bars
    for i,dat in enumerate(data):
        x_temp = ind
        print x_temp
        print dat
        temp_color = color_set[i]
        ax.bar(x_temp, dat, width, color=temp_color)
        ind += width
    # Backround
    ax.set_axis_bgcolor('white') 
    # Title Options
    if xlab is not None:
        ax.set_xlabel(xlab)
    if ylab is not None:
        ax.set_ylabel(ylab)
    if main is not None:
        ax.set_title(main)
    # Ticks
    ax.set_xticks( ind - off + width/2. )
    tick_labels = []
    for i in range( nprob ):
        tick_labels.append( "P" + str( i+1 ) )
    ax.set_xticklabels(tick_labels)

 
    
    plt.show()


data = [[0.5,0.5],[0.1,0.9]]
barplot(data)
