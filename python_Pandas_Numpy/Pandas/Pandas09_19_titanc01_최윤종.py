
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[3]:


titanic = sns.load_dataset('titanic')


# In[4]:


print(titanic.columns)
print(len(titanic.columns))


# In[5]:


for idx in titanic.columns:
    print("[%s]\n" %idx)
    print(titanic[idx].unique())
    print("="*80)

