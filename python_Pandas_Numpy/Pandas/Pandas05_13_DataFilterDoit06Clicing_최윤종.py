
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep = "\t")


# In[3]:


df.head(3)


# In[4]:


print(df.iloc[[0, 99,999],[0,3,5]])


# In[6]:


print(df.loc[[0,99,999],['country','lifeExp','gdpPercap']])


# In[7]:


print(df.loc[10:13,['country','lifeExp','gdpPercap']])


# In[8]:


print(df.iloc[10:13,[0,3,-1]])

