
# coding: utf-8

# In[8]:


import pandas


# In[9]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[10]:


print(df.groupby('continent')['year'].count())


# In[11]:


uniList = df['continent'].unique()
print(type(uniList))
print(uniList, "\n =====>")


# In[20]:


for idx in uniList:
    print(idx, "=====> 1:")
    grContinent = df[df['continent'] == idx]
    print(len(grContinent), "\n =====> 2:" , grContinent.head(3), "\n=====> 3:", grContinent.shape)
   

