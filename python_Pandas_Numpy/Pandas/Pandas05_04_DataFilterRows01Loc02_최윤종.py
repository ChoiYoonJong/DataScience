
# coding: utf-8

# In[23]:


import pandas as pd


# In[24]:


df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
df


# In[25]:


df.loc[['viper','sidewinder'], ['shield']] = 50
df


# In[26]:


df.loc[:, 'max_speed'] = 30
df


# In[28]:


df.loc[df['shield'] > 35] = 0
df


# In[31]:


df = pd.DataFrame([[1,2],[4,5],[7,8]],
      index=[7,8,9], columns=['max_speed', 'shield'])
df


# In[32]:


df.loc[7:9]

