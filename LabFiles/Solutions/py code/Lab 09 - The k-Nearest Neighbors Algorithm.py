
# coding: utf-8

# In[1]:


import sklearn as sk
import numpy as np
import pandas as pd


# In[2]:


sk.__version__


# In[3]:


input_file = 'http://bit.ly/2O7Islk'
all = pd.read_csv(input_file, header=None, sep=',')
all.head()


# In[4]:


len (all)


# In[5]:


c = all.loc[:,[57]]
c[c == 1].count(),  c[c == 0].count()


# In[6]:


spamdb = all.loc[:, 0:56]


# In[7]:


from sklearn.model_selection import train_test_split


# In[8]:


labels = np.concatenate([[1 for i in range(1813)], [0 for i in range(2788)]])


# In[9]:


data_train, data_test, label_train, label_test = train_test_split(spamdb, labels, test_size=0.3, random_state=0)


# In[14]:


from sklearn.neighbors import KNeighborsClassifier
knnModel = KNeighborsClassifier(n_neighbors=3)
knnModel.fit(data_train, label_train) 


# In[15]:


label_predict = knnModel.predict(data_test)


# In[16]:


import sklearn.metrics as metrics
metrics.confusion_matrix(label_test, label_predict)


# In[17]:


knnModel.score(data_train, label_train)


# In[18]:


knnModel.score(data_test, label_test)

