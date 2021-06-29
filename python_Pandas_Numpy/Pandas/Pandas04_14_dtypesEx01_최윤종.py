
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame({'float':[1.0],
                   'int':[1],
                   'datatime': [pd.Timestamp('20180310')],
                   'string':['foo']})
print(df)
df.dtypes

