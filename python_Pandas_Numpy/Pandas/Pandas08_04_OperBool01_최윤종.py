
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


scientists = pd.read_csv('../data/scientists.csv')


# In[6]:


ages = scientists['Age']

print(ages.max())


# In[7]:


print(ages.mean())


# In[8]:


print(ages[ages > ages.mean()])


# In[9]:


print(ages > ages.mean())


# In[10]:


print(type(ages > ages.mean()))


# In[13]:


manual_bool_values = [True,True,False,False,True,True,False,True]
print(ages[manual_bool_values])

