#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import urllib.request as webreq
import os

local_files =  ["c:/Works/training_two_classes.svm", "c:/Works/test_two_classes.svm"]

urls = ['http://bit.ly/37FTdmY', 'http://bit.ly/2tLzzqV']

for f_name, url in zip(local_files, urls):
    if not os.path.exists (f_name):
        http_msg = webreq.urlretrieve (url, f_name) 


# In[3]:


from sklearn.datasets import load_svmlight_file
trainData, trainLabels = load_svmlight_file("training_two_classes.svm")


# In[4]:


trainLabels


# In[5]:


from sklearn.ensemble import RandomForestClassifier

RFModel = RandomForestClassifier(n_estimators=3, random_state=1).fit(trainData, trainLabels)


# In[6]:


RFModel


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from sklearn import tree

plt.figure(figsize=(12,12))

tree.plot_tree(RFModel.estimators_[0], class_names= ['A', 'B']);  


# In[10]:


tree.plot_tree(RFModel.estimators_[1], class_names= ['A', 'B']); 


# In[11]:


tree.plot_tree(RFModel.estimators_[2], class_names= ['A', 'B']); 


# In[12]:


RFModel.predict([[0,0], [10,9], [2,5], [19,18], [15,16]])


# In[13]:


testData, testLabels = load_svmlight_file("c:/Works/test_two_classes.svm")


# In[14]:


testData.toarray()


# In[15]:


testLabels


# In[16]:


predictedLabels = RFModel.predict(testData)


# In[17]:


import sklearn.metrics as metrics
metrics.confusion_matrix(testLabels, predictedLabels)


# In[18]:


testLabels[-1] = 0; testLabels


# In[19]:


metrics.confusion_matrix(testLabels, predictedLabels)


# In[ ]:




