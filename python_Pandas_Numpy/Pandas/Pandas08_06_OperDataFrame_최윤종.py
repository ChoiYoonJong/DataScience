
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


scientists = pd.read_csv('../data/scientists.csv')


# In[7]:


print(scientists[scientists['Age'] > scientists['Age'].mean()])


# In[8]:


print(scientists.loc[[True,True,False,True]])


# In[9]:


print(scientists * 2)

