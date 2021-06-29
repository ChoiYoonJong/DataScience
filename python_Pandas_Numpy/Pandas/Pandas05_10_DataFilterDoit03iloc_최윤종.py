
# coding: utf-8

# In[1]:


import pandas


# In[3]:


df = pandas.read_csv('../data/gapminder.tsv', sep ='\t')


# In[4]:


print(df.head(3))


# In[5]:


print(df.iloc[1])


# In[6]:


print(df.iloc[99])


# In[7]:


print(df.iloc[-1])


# In[8]:


print(df.tail(1))
print(df.shape)
print(df.iloc[1703])


# In[11]:


print(df.iloc[[0, 99, 999]])

