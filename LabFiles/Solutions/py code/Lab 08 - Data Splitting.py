
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from sklearn.model_selection import ShuffleSplit
initDS = np.arange(20)
splitter = ShuffleSplit(n_splits=4, test_size=0.2, random_state=0)
for trainDS, testDS in splitter.split(initDS):
   print(trainDS, testDS)


# In[3]:


initDS = np.arange(100).reshape(5,20)
splitter = ShuffleSplit(n_splits=4, test_size=0.4,random_state=0)
for trainDS, testDS in splitter.split(initDS):
   print(trainDS, testDS)


# In[4]:


initDS


# In[5]:


input_file = 'http://bit.ly/36w1jgf'
all = pd.read_csv(input_file, header=None, sep=',')
all.head(2), all.tail(2)


# In[6]:


labels = [int(i) for i in (10 * '1' + 10 * '0')]
len(labels)


# In[7]:


from sklearn.model_selection import train_test_split
data_train, data_test, label_train, label_test = train_test_split(all, labels, test_size=0.4, random_state = 0)


# In[8]:


data_train, data_test, label_train, label_test 

