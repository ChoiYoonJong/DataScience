#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

scientists = pd.DataFrame(
    data={'Occupation':['Chemist','Statistician'],
        'Born':['1920-07-25','1876-06-13'],
        'Died':['1958-04-16','1937-10-16'],
        'Age':[37,61]},
    index=['Rosaline Franklin','William Gosset'],
    columns=['Occupation','Born',"Age",'Died'])
    
print(scientists)


# In[4]:


first_row = scientists.loc['William Gosset']
print(type(first_row))


# In[5]:


print(first_row)


# In[6]:


print(first_row.index)


# In[7]:


print(first_row.values)


# In[8]:


print(first_row.keys)


# In[9]:


print(first_row.index[0])


# In[10]:


print(first_row.keys()[0])


# In[11]:


print(scientists,'\n\n')

ages = scientists['Age']
print(ages)


# In[13]:


print(ages.mean())


# In[14]:


print(ages.min())


# In[15]:


print(ages.max())


# In[16]:


print(ages.std())

