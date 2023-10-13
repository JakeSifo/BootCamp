
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


import random
random.seed(777)
v = [random.randint(-5,5) for k in range(20)]
plt.figure(figsize=[12,8])
plt.title("A simple plot", size = 'x-large')
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.plot(v, 'g-', linewidth = 6 );


# In[11]:


random.seed(111)
mean, std = 0, 1
X = [random.gauss(mean, std) for i in range(1500)] 
plt.xlabel('Measurement')
plt.ylabel('Probability')
plt.title('Histogram of Measurements')
plt.grid(True)
plt.hist(X, 100, density=True, facecolor='b');


# In[12]:


plt.subplot(222)
plt.plot(range(20), 'r+')
plt.subplot(221)
plt.plot(range(40), 'g.')
plt.subplot(224)
plt.plot(range(60), 'bx')
plt.subplot(223)
plt.plot(range(100),'c-' )


# In[13]:


plt.plot(range(20), 'r+')
plt.savefig('simple_line.jpeg', dpi=600)


# In[14]:


sns.set()


# In[15]:


input_file = 'http://bit.ly/36je2mw' 
cars = pd.read_csv(input_file); cars.head(4)


# In[16]:


cars.index


# In[17]:


cars.columns


# In[18]:


cars.info()


# In[20]:


sns.distplot (cars.hp, color='g', bins=20) ; 


# In[21]:


sns.jointplot(x="hp", y="wt", data=cars, kind="kde");


# In[22]:


sns.boxplot(cars.qsec, orient='v', palette='summer');


# In[23]:


cars[cars.qsec > 22]


# In[24]:


sns.catplot(x='gear', y = 'mpg', data = cars);


# In[25]:


pd.unique(cars.cyl)


# In[26]:


sns.catplot(x='gear', y = 'mpg', data = cars, hue = 'cyl'); 


# In[27]:


sns.catplot(x='gear', y = 'mpg', kind='box', data = cars);


# In[28]:


columns = ['hp', 'wt', 'mpg', 'cyl', 'disp', 'qsec']
df = cars [columns].copy() 


# In[29]:


sns.pairplot(df);     


# In[30]:


sns.set()
sns.heatmap(df.corr());

