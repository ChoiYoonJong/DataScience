#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df,'\n')
print("="*50)

df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df, '\n')
print("="*50)

ndf = df.reset_index()
print(ndf)


# In[9]:


import pandas as pd

dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data)
print(df,'\n')

df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df,'\n')

ndf = df.reset_index()
print(ndf)


# In[ ]:




