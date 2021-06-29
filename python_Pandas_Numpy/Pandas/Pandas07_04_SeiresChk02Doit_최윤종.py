#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
s = pd.Series(['banana',42])
print(s)


# In[2]:


s = pd.Series(['Wes McKinney','Creator of Pandas'])
print(s)


# In[11]:


s = pd.Series(['Wes McKinney','Creator of Pandas'], index=['Person','Who'])
print(s)


# In[3]:


scientists = pd.DataFrame({
    'Name':['Rosaline Frankin','William Gosset'],
    'Occipation':['Chemist','Statistician'],
    'Born':['1920-07-25','1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]})
print(scientists)


# In[5]:


scientists = pd.DataFrame(
    data={'Occupation':['Chemist','Statistician'],
        'Born':['1920-07-25','1876-06-13'],
        'Died':['1958-04-16','1937-10-16'],
        'Age':[37,61]},
    index=['Rosaline Franklin','William Gosset'],
    columns=['Occupation','Born',"Age",'Died'])
    
print(scientists)


# In[14]:


from collections import OrderedDict

scientists = pd.DataFrame([
    ('Name',['Roasline Franklin','William Gosset']),
    ('Occupation',['Chemist','Statistician']),
    ('Born',['1920-07-25','1876-06-13']),
    ('Died',['1958-04-16','1937-10-16']),
    ('Age',[37,61])
])
print(scientists)
print(type(scientists[0]))


# In[18]:


from collections import OrderedDict

scientists = pd.DataFrame(OrderedDict([
    ('Name',['Roasline Franklin','William Gosset']),
    ('Occupation',['Chemist','Statistician']),
    ('Born',['1920-07-25','1876-06-13']),
    ('Died',['1958-04-16','1937-10-16']),
    ('Age',[37,61])
])
)
print(scientists)


# In[ ]:




