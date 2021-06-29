
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[5]:


print(df.groupby('continent')['year'].nunique(),"\n====>")
print(df.groupby('continent')['year'].unique(),"\n====>")
print(df.groupby('continent')['year'].unique()['Africa'],"\n====>")

