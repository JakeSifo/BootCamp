#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import KMeans
import numpy as np
import pandas as pd


# In[2]:


input_file = 'http://bit.ly/315EqiY'
df=pd.read_csv(input_file, sep=' ', header=None)
df.head()


# In[3]:


kmeansModel = KMeans(n_clusters=3, random_state=0).fit(df)


# In[4]:


kmeansModel


# In[5]:


kmeansModel.cluster_centers_


# In[6]:


kmeansModel.predict ([[1,3]])


# In[7]:


kmeansModel.predict([[6, 7], [11, 8]])


# In[8]:


kmeansModel.labels_


# In[10]:


list(kmeansModel.labels_).count(1)


# In[11]:


kmeansModel.inertia_


# In[12]:


km2 = KMeans(n_clusters=3, random_state=0, n_init=1, tol = 1).fit(df) 
km2.inertia_


# In[13]:


kmeansModel.labels_ - km2.labels_ 


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.title("Visualizing kmeans ...")
plt.scatter(df[0], df[1], c=kmeansModel.labels_, cmap = 'Dark2_r');


# In[16]:


import seaborn as sns
sns.set()
sns.scatterplot(df[0], df[1], hue=km2.labels_);


# In[17]:


input_file = 'http://bit.ly/2O7Islk'
all = pd.read_csv(input_file, header=None, sep=',')


# In[18]:


true_labels = all[57]


# In[20]:


kspam = KMeans(n_clusters=2, random_state=0).fit(all)

import sklearn.metrics as metrics
metrics.confusion_matrix(true_labels,kspam.labels_)


# In[21]:


kspam.inertia_


# In[22]:


#Use kNN
from sklearn.neighbors import KNeighborsClassifier
knnModel = KNeighborsClassifier(n_neighbors=3)
knnModel.fit(all, true_labels)


# In[23]:


label_predict_0 = knnModel.predict(kspam.cluster_centers_[0].reshape(1,-1)); 
label_predict_1 = knnModel.predict([kspam.cluster_centers_[1]]);
label_predict_0, label_predict_1


# In[25]:


# Use Random Forest
from sklearn.ensemble import RandomForestClassifier


# In[26]:


RFModel = RandomForestClassifier(n_estimators=3, random_state=1).fit(all, true_labels)


# In[27]:


label_predict_rf0 = RFModel.predict(kspam.cluster_centers_[0].reshape(1,-1))
label_predict_rf1 = RFModel.predict(kspam.cluster_centers_[0].reshape(1,-1))
label_predict_rf0, label_predict_rf1


# In[ ]:




