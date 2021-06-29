
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv',sep='\t')


# In[9]:


multi_group_var = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()
print(multi_group_var.head(3))
df.groupby(['year','continent']).mean().head()


# In[10]:


print(multi_group_var)

