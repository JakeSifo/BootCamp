#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb


# In[2]:


xgb.__version__


# In[3]:


data = "housing_prices_data.csv"
XAll = pd.read_csv(data, index_col='Id')
XAll.shape


# In[4]:


XAll.columns


# In[5]:


XAll[:20]


# In[6]:


y = XAll.SalePrice  


X = XAll.drop(['SalePrice'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y,  train_size=0.8, test_size=0.2, random_state=0) 


# In[7]:


print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)


# In[8]:


X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)


# In[9]:


print (X_train.shape, X_test.shape)


# In[10]:


X_train2, X_test2 = X_train.align(X_test, join='left', axis=1)


# In[11]:


print (X_train2.shape, X_test2.shape)


# In[12]:


import warnings
warnings.filterwarnings('ignore')

xgb_model = xgb.XGBRegressor (objective='reg:squarederror',  random_state=7777)

xgb_model.fit(X_train2, y_train)


# In[13]:


predictions = xgb_model.predict(X_test2)


# In[18]:


from sklearn.metrics import mean_absolute_error
print ("The MEA: " + str(mean_absolute_error(predictions, y_test)))


# In[19]:


xgb_model.score (X_train2, y_train)


# In[16]:


xgb_model2 = xgb.XGBRegressor (objective='reg:squarederror',  random_state=7777, n_estimators=200)


# In[20]:


xgb_model.feature_importances_


# In[ ]:




