
# coding: utf-8

# In[1]:


type(None)


# In[2]:


None == None


# In[3]:


import numpy as np
np.__version__ 


# In[4]:


get_ipython().run_line_magic('pinfo', 'dir')


# In[5]:


dir(np)


# In[9]:


i = '1234567'
i[0:3]


# In[10]:


i[-1]


# In[11]:


s  = '123.45'
f = float(s); print (f)
i = int(i); print (i)
s2 = str(i)


# In[12]:


for k in range(5):
    print (k)


# In[6]:


key2 = '_key2'
d = { '_key1': 123, key2: 456 } ; d


# In[7]:


d[key2] += d['_key1']; d


# In[5]:


list_of_str = 'as easy as A B C'.split()


# In[6]:


d = {}
for k, v in enumerate(list_of_str):
  d[k] = v

d


# In[7]:


list(d.keys())
list(d.values())
dt = list(d.items()); dt


# In[8]:


type(dt[0])


# In[9]:


dt[2][1] = 'like';


# In[11]:


debug


# In[10]:


type(dt[2])


# In[12]:


def f():
   print ("Calling f()")    
   return True 

def g():
   print ("Calling g()")
   return False


# In[13]:


f() and g()


# In[14]:


b = f() or g()


# In[15]:


def make_a_list (* items):
    return items


# In[16]:


lmap = list (map(lambda x: x * x, [1,2,3,4,5])); lmap


# In[17]:


get_ipython().run_cell_magic('timeit', 'l1 = []', 'l1.append (map(lambda x: x * x, [1,2,3,4,5]))')


# In[18]:


get_ipython().run_cell_magic('timeit', 'l2 = []', 'for v in [1,2,3,4,5]:\n  l2.append( v * v )')


# In[19]:


x = [1,2,3,4,5]
y = [10,20,30,40,50]
z = ['a','b','c','d','e']

[z + '->' + str(x) + ':' + str(y) for x, y, z in zip(x,y,z)]


# In[20]:


[ i**2 for i in range (1, 5) if (i % 2 == 0) ]

