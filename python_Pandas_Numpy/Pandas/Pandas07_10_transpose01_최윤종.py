#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

exam_data = {'이름':['서준','우현','인아'],
            '수학':[90,80,70],
            '영어':[98,89,95],
            '음악':[85,95,100],
            '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df,'\n')
print("="*50)

df = df.transpose()
print(df,'\n')
print("="*50)

df = df.T
print(df)


# In[ ]:




