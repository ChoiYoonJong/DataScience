
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


titanic = sns.load_dataset('titanic')


# In[3]:


titanic['survived'].unique()


# In[4]:


titanic['sex'].unique()


# In[5]:


#성별 생존률의 개수

q5_survived_cnt = titanic[titanic['survived'] == 1]

q5_survived_cnt.groupby('sex')['survived'].count()

