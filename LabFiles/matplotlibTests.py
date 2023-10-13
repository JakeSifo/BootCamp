import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec



# Using the GridSpec
#from matplotlib.gridspec import GridSpec


# plt.pie([5,45,20,30], autopct='%1.1f%%', 
#     colors=["r", "#00FF00", "b", "c"],
#     radius=0.6, labels=['W', 'X', 'Y', 'Z'])

def usingGridSpec():
    grid = GridSpec (2,2)


    plt.subplot(grid[0,0], aspect = 1)
    plt.pie([100], colors=["#111111"], labels = ['grid[0,0]'], radius=0.3)

    plt.subplot(grid[0,1], aspect = 1)
    plt.pie([100], colors=["#666666"], labels = ['grid[0,1]'], radius=0.3)

    plt.subplot(grid[1,0], aspect = 1)
    plt.pie([100], colors=["#AAAAAA"], labels = ['grid[1,0]'], radius=0.3)

    plt.subplot(grid[1,1], aspect = 1)
    plt.pie([100], colors=["#EEEEEE"], labels = ['grid[1,1]'], radius=0.3)

    plt.show()


#usingGridSpec()

def griddingWithSubplot():
    # now create a subplot which represents the top plot of a grid
# with 2 rows and 1 column. Since this subplot will overlap the
# first, the plot (and its axes) previously created, will be removed
    plt.subplot(222) #, 'r') #  a = fig.add_subplot(*args, **kwargs)
    plt.plot(range(20), 'r+')
    plt.subplot(221) #, color='g')
    plt.plot(range(40), 'g.')
    plt.subplot(224) #, color='b')
    plt.plot(range(60), 'bx')
    plt.subplot(223) #, color='y')
    plt.plot(range(100),'c-' )
    plt.show()

#griddingWithSubplot()

def sineDemo():
    t = np.arange(0.0, 2.0, 0.01)
    s1 = np.sin(2*np.pi*t)
    s2 = np.sin(4*np.pi*t)
    plt.figure("Figure one")
    plt.subplot(211)
    plt.plot(t, s1)
    plt.subplot(212)
    plt.plot(t, 2*s1)  
    
    plt.figure("Figure two")
    plt.plot(t, s2)

    plt.show()

#sineDemo()

def saveFig():
    plt.plot(range(20), 'r+')
    plt.savefig('img/justLine.jpeg', dpi=600)

# saveFig()

def simplePlot():
    data = [ x**2 for x in range(9)]
    plt.figure()
    plt.plot(data)

simplePlot()