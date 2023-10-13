
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


np.random.seed(10)
sales = np.array((100 * np.random.rand (5)).astype(int))
sales


# In[3]:


location = [c for c in 'ABCDE']; location


# In[4]:


data_np = np.array([sales, location])
data_np


# In[5]:


df = pd.DataFrame(data_np, columns = ["Sales", "Location"])


# In[8]:


data_np = np.array([sales, location]).T
data_np


# In[10]:


df = pd.DataFrame(data_np, columns = ["Sales", "Location"])
df


# In[15]:


df.dtypes


# In[16]:


df.Sales = df.Sales.astype(int)


# In[17]:


df.describe()


# In[18]:


df.Location


# In[45]:


df.Sales


# In[46]:


df.loc[:2, 'Location'] 


# In[47]:


df.iloc[-1, :]


# In[48]:


df.Sales.sort_values(ascending=False)


# In[49]:


df['Month'] = pd.DataFrame(['Jan', 'Feb', 'Mar', 'Apr', 'May']); df


# In[54]:


del df['Month']


# In[57]:


df1 = df.head()
df2 = df.tail()
df12 = pd.concat([df1, df2])
df12


# In[61]:


df12 = pd.concat([df1, df2], ignore_index=True); df12 


# In[73]:


url = 'http://bit.ly/36fGR32'
df2 = pd.read_csv(url)


# In[74]:


df2.head()


# In[75]:


df2.info()


# In[76]:


df2.columns


# In[78]:


df2.index


# In[79]:


df2.dtypes


# In[81]:


df2.DAY = df2.DAY.astype(np.int32)
df2.FSIZE = df2.FSIZE.astype(np.int32) 


# In[82]:


df2.dtypes

