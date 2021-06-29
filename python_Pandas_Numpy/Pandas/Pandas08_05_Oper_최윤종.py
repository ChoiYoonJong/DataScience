
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('../data/scientists.csv')


# In[3]:


ages = scientists['Age']

print(ages.max())


# In[5]:


print(ages + ages)


# In[6]:


print(ages * ages)


# In[7]:


print(ages + 100)


# In[8]:


print(ages * 2)


# In[9]:


print(pd.Series([1,100]))


# In[10]:


print(ages,"\n\n")

print(pd.Series([1,100]),"\n\n")

print(ages + pd.Series([1,100]))


# In[11]:


print(ages)


# In[14]:


rev_ages = ages.sort_index(ascending=False)
print(rev_ages)


# In[15]:


print(ages * 2)


# In[16]:


print(ages + rev_ages)

