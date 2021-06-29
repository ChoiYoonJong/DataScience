
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep="\t")


# In[3]:


print(df.groupby('continent')['country'])


# In[5]:


print(df.groupby('continent')['country'].nunique())

print(df.groupby('continent')['country'].unique())

print(df.groupby('continent')['country'].unique()['Oceania'])

print(df.groupby('continent')['country'].count())

print(df.groupby('continent')['country'].count()['Africa'])

