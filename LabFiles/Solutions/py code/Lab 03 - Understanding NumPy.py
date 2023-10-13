
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


python_list = [1,2,3,4,5]
np_array = np.array( python_list )


# In[4]:


type(np_array[0])


# In[5]:


np_int64 = np.array( [1,2,3], dtype = np.int64)
type(np_int64[0])


# In[6]:


np.arange(12) 


# In[7]:


np.arange(12).shape


# In[8]:


t = 12
print(type(t))
t = 12,
print(type(t))
print(t)


# In[9]:


m = np.arange(12).reshape(3,4); m


# In[10]:


np_array % 2 == 0


# In[11]:


np_array [np_array <= 3]


# In[12]:


import numpy as np
np.random.seed(10)
sales = np.array((100 * np.random.rand (5)).astype(int)); sales

