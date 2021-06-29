
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
df


# In[5]:


df.loc['viper'] #df.iloc[0]


# In[6]:


df.loc[0]


# In[7]:


df.loc[['viper','sidewinder']]


# In[14]:


df.loc['cobra','shield']


# In[9]:


df.loc['cobra':'viper', 'max_speed']


# In[10]:


df.loc[[False, False, True]]


# In[11]:


df.loc[df['shield']>6]


# In[12]:


df.loc[df['shield']>6,['max_speed']]

