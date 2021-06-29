#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

exam_data = {'이름':['서준','우현','인아'],
            '수학':[90,80,70],
            '영어':[98,89,95],
            '음악':[85,95,100],
            '체육':[100,90,90]}
df = pd.DataFrame(exam_data)
print(df,'\n')

df['국어']=80
print(df)


# In[6]:


import pandas as pd

exam_data = {'이름':['서준','우현','인아'],
            '수학':[90,80,70],
            '영어':[98,89,95],
            '음악':[85,95,100],
            '체육':[100,90,90]}

df=pd.DataFrame(exam_data)
print(df,'\n')

df.loc[3]=0
print(df,'\n')

df.loc[4] = ['동규',90,80,70,60]
print(df,'\n')

df.loc['행5'] = df.loc[3]
print(df)


# In[ ]:




