
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


input_file =  'http://bit.ly/2U18s5V' 
ship = pd.read_csv(input_file); ship.head(4)


# In[4]:


ship.shape


# In[5]:


ship.info()


# In[6]:


ship = ship.rename(columns = {'Siblings/Spouses Aboard': 'SibSp', 'Parents/Children Aboard' : 'Parch' }); ship.columns


# In[7]:


ship.Survived = ship['Survived'].astype('category')
ship['Pclass'] = ship.Pclass.astype('category')


# In[8]:


sns.set()
sns.distplot (ship.Fare, color='g', bins=20) ; 


# In[9]:


plt.figure(figsize=[14,3])
sns.boxplot(ship.Fare);


# In[10]:


ship [ship.Fare > 500]


# In[11]:


sns.catplot(x='Survived', y = 'Fare', data = ship, hue='Pclass');


# In[13]:


cols = ['Survived', 'Pclass', 'Sex', 'Age', 'Fare']
df = ship [cols].copy()


# In[14]:


sns.pairplot(df, hue='Survived'); 


# In[15]:


ship[ship.Age > 70]

