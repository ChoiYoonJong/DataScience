#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd

exam_data ={'수학':[90,80,70], '영어':[98,89,95],
           '음악':[85,95,100],'체육':[100,90,90]}

df = pd.DataFrame(exam_data, index=['서준','우현','안아'])
print(df,'\n')

label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1,'\n')
print(position1,'\n')


# In[9]:


label2 = df.loc[["서준","우현"]]
position2 = df.iloc[[0,1]]
print(label2,'\n')
print(position2,'\n')

label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print(label3,'\n')
print(position3)


# In[11]:


### 1.10


# In[21]:


import pandas as pd

exam_data = {'이름': ['서준','우현','인아'],
            '수학':[90,80,70],
            '영어':[98,89,95],
            '음악':[85,95,100],
            '체육':[100,90,90]}

df=pd.DataFrame(exam_data)
print(df,'\n')
print(type(df),'\n')

math1 = df['수학']
print(math1,'\n')
print(type(math1),'\n')

english = df.영어
print(english,'\n')
print(type(english),'\n')


# In[16]:


music_gym = df[['음악','체육']]
print(music_gym,'\n')
print(type(music_gym),'\n')

math2 = df[['수학']]
print(math2,'\n')
print(type(math2))


# In[17]:


math2 = df['수학']
print(math2,'\n')
print(type(math2))


# In[ ]:




