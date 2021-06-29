
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep ='\t')


# In[3]:


df.head(3)


# In[4]:


subset = df.loc[:,['year','pop']]
print(subset.head())


# In[5]:


subset = df.iloc[:,[2,4,-1]]
print(subset.head())

