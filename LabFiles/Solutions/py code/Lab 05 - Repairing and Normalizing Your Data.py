
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


input_file = 'http://bit.ly/36gJKAM'
dataSet  = pd.read_csv(input_file, header=None, names = ['C1', 'C2', 'C3', 'C4']); dataSet


# In[3]:


dataSet.isnull().sum(axis = 0)


# In[4]:


dataSet2 = dataSet.drop('C1', axis=1) 


# In[5]:


dataSet2.shape


# In[6]:


dataSet2.isnull().sum(axis = 1)


# In[7]:


dataSet3 = dataSet2.drop(2, axis=0)


# In[9]:


dataSet3.dropna()


# In[10]:


dataSet4 = dataSet3.copy() 


# In[11]:


dataSet4.C3.interpolate (inplace=True)


# In[12]:


dataSet4.C4.interpolate (method='nearest', inplace=True); dataSet4.C4


# In[13]:


dataSet5 = dataSet3.copy()
dataSet5.C3.fillna(dataSet5.C3.mean(), inplace=True)
dataSet5


# In[14]:


dataSet5.index = range(dataSet5.shape[0])


# In[15]:


print (dataSet5.iloc[2])
print ('...................')
print (dataSet5.iloc[2].mean())


# In[16]:


dataSet5.iloc[2].fillna(dataSet5.iloc[2].mean(), inplace=True)


# In[20]:


dataSet5.C4.fillna(dataSet5.C4.mean(), inplace=True); dataSet5


# In[21]:


from sklearn import preprocessing


# In[22]:


dataSet5_scaled = preprocessing.scale(dataSet5); dataSet5_scaled


# In[23]:


np.random.seed(1234)
toScaleDS = np.ceil(100 * np.random.rand (10,3))
toScaleDS


# In[24]:


from sklearn import preprocessing
scaledDS = preprocessing.scale(toScaleDS)
scaledDS


# In[25]:


np.mean(scaledDS, axis = 0)


# In[26]:


np.std(scaledDS, axis = 0)


# In[27]:


mmScaler = preprocessing.MinMaxScaler()
mmScaler.fit_transform(toScaleDS)

