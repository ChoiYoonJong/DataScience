
# coding: utf-8

# In[1]:


import pandas


# In[3]:


df = pandas.read_csv('../data/gapminder.tsv',sep='\t')


# In[7]:


multi_group_var = df.groupby(['year','continent'])['lifeExp']
print(multi_group_var)
#print(multi_group_var.mean().head())
print(multi_group_var.mean())
print(multi_group_var.mean().count())
# 5 * 12

