
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('../data/scientists.csv')


# In[3]:


print(scientists['Age'])


# In[5]:


import random

random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])

