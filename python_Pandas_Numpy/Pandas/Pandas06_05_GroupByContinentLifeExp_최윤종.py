
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep ="\t")


# In[4]:


uniList = df['continent'].unique()
for idx in uniList:
    print(idx, "==========>① :")
    grCon = df[df['continent']==idx]
    print(grCon['pop'].mean())


# In[12]:


grouped_continent_df = df.groupby('continent')
print(type(grouped_continent_df))
print(grouped_continent_df['pop'])


# In[8]:


grouped_continent_df['pop'].mean()

