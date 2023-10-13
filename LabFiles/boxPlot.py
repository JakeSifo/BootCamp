import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import random



################################################
# Showing the outliners (EDA)
################################################

events = np.random.exponential (0.5, 200)
# print(events)
#mean
plt.figure("Direct call to plt.boxplot()...")
plt.boxplot(events)    # A call to plt.figure() is done implicitly


plt.figure("Direct call to plt.boxplot()...with GRID true")
plt.grid(True)  # Show the axes grids
plt.boxplot(events)    # A call to plt.figure() is done implicitly


plt.figure("Using panda's matplotlib intreface")
df = pd.DataFrame(events)
# To see the structure of the df:
# print(df.head())
# Should reveal something like this:
#           0
# 0  0.226820
# 1  0.416316
# 2  0.292084
# 3  0.038870
# 4  0.063974

# The column name is '0'

df.boxplot(0, return_type='axes')

plt.show() 



