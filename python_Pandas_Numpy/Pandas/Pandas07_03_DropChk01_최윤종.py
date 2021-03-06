#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


exam_data = {'수학': [90,80,70], '영어':[98,89,95],
            '음악':[85,95,100], '체육':[100,90,90]}

df = pd.DataFrame(exam_data)
print(df,'\n')
print("-"*50)

df= pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df,"\n")
print("-"*50)

df2= df[:]
df2.drop('우현',inplace=True)
print(df2,"\n")
print("-"*50)

df3 = df[:]
df3.drop(['우현','인아'],axis=0, inplace=True)
print(df3)


# In[6]:


import pandas as pd

exam_data = {'수학': [90,80,70], '영어':[98,89,95],
            '음악':[85,95,100], '체육':[100,90,90]}

df = pd.DataFrame(exam_data)
print(df,'\n')

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df,"\n")

df4=df[:]
df4.drop('수학',axis=1, inplace=True)
print(df4,"\n\n")

df5 = df[:]
df5.drop(['영어','수학'], axis=1, inplace=True)
print(df5)


# In[ ]:




