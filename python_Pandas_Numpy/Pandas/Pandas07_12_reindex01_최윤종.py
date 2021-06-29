#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df,'\n')

new_index = ['r0','r1','r2','r3','r4']
ndf = df.reindex(new_index)
print(ndf,'\n')

new_index = ['r0','r1','r2','r3','r4']
ndf2= df.reindex(new_index, fill_value=0)
print(ndf2)


# In[ ]:




