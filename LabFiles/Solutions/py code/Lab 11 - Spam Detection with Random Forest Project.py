#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn as sk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics


# In[2]:


input_file = 'http://bit.ly/2O7Islk'
all = pd.read_csv(input_file, header=None, sep=',')
spamdb = all.loc[:, 0:56]
labels = all[57]

data_train, data_test, label_train, label_test = train_test_split(spamdb, labels, test_size=0.3, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
knnModel = KNeighborsClassifier(n_neighbors=3)
knnModel.fit(data_train, label_train)
label_predict = knnModel.predict(data_test)
metrics.confusion_matrix(label_test, label_predict)


# In[3]:


score_knn_train = knnModel.score(data_train, label_train)
score_knn_test = knnModel.score(data_test, label_test)
print (score_knn_train, score_knn_test)


# In[4]:


from sklearn.ensemble import RandomForestClassifier

RFModel = RandomForestClassifier(n_estimators=3, random_state=1).fit(data_train, label_train)

label_predict = RFModel.predict(data_test)
metrics.confusion_matrix(label_test, label_predict)

score_rf_train = RFModel.score(data_train, label_train)
score_rf_test = RFModel.score(data_test, label_test)
print (score_rf_train, score_rf_test)


# In[5]:


get_ipython().run_line_magic('timeit', 'knnModel.predict(data_test)')
get_ipython().run_line_magic('timeit', 'RFModel.predict(data_test)')


# In[ ]:




