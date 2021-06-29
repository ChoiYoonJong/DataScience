#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

exam_data = {'이름': ['서준','우현','인아'],
            '수학':[90,80,70],
            '영어':[98,89,95],
            '음악':[85,98,100],
            '체육':[100,90,90,]}
df = pd.DataFrame(exam_data)
print(df,'\n')

df.set_index('이름',inplace=True)
print(df,'\n')

a=df.loc['서준','음악']
print(a,'\n')
b = df.iloc[0,2]
print(b,'\n')


# In[2]:


c = df.loc['서준',['음악','체육']]
print(c,'\n')
d= df.iloc[0,[2,3]]
print(d,'\n')
e = df.loc['서준','음악':'체육']
print(e,'\n')
f = df.iloc[0,2:]
print(f,'\n')

g = df.loc[['서준','우현'],['음악',"체육"]]
print(g,'\n')
h = df.iloc[[0,1],[2,3]]
print("df.iloc[[0,1],[2,3]]\n",h,'\n')
i =df.loc['서준':'우현','음악':'체육']
print('df.loc["서준","우현","음악":"체육"]\n',i,'\n')
j = df.iloc[0:2,2:]
print(j)


# In[3]:


df.loc[:,['음악','체육']]


# In[4]:


print(df)
df.iloc[:,[2,3]]


# In[5]:


df.iloc[:,2:4]


# In[ ]:




