
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('../data/scientists.csv')


# In[3]:


scientists


# In[4]:


print(scientists['Born'].dtype)
print(scientists['Died'].dtype)


# In[12]:


born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datetime)


# In[14]:


died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(born_datetime)


# In[15]:


died_datetime2 = died_datetime - born_datetime


# In[16]:


print(died_datetime2)


# In[17]:


scientists['born_dt'],scientists['died_dt'] = (born_datetime,died_datetime)
print(scientists.head())


# In[20]:


print(scientists.shape)


# In[23]:


scientists['age_days_dt']=(scientists['died_dt'] -                           scientists['born_dt'])
print(scientists)

