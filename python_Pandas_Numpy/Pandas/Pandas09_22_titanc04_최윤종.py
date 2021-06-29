
# coding: utf-8

# In[19]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[20]:


titanic = sns.load_dataset('titanic')


# In[42]:


ages = list(range(0,90,10))

for x in ages:
    start =x
    end = x + 10
    ageTemp = titanic[(titanic['age']>= start) & (titanic['age'] < end)]
    print("{}세 이상 - {}세미만 사망자수:{}".format(start,end,(ageTemp['survived']).count() ))


# In[43]:


ages = list(range(0,90,10))

for x in ages:
    start =x
    end = x + 10
    ageTemp = titanic[(titanic['age']>= start) & (titanic['age'] < end)]
    print(ageTemp['sex'][ageTemp['survived']==0].count(), ageTemp['sex'][ageTemp['survived']==1].count())
    print("{}세 이상 - {}세미만 사망자수:{}".format(start,end,(ageTemp['sex'][ageTemp['survived']==0].count() )))

