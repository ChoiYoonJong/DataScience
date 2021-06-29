
# coding: utf-8

# In[4]:


import pandas


# In[5]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[6]:


print(df.groupby('year')['lifeExp'].mean())


# In[9]:


df['year'].unique()


# In[10]:


uniList = df['year'].unique()
print(type(uniList))
print(uniList,"\n====>")


# In[11]:


for idx in uniList:
    print(idx, "=====> 1 :")
    grYear = df[df['year'] == idx]
    print(len(grYear), "\n ====> 2 \n:", grYear.head(3), "n =====> 3 :", grYear.shape)
    print(grYear["lifeExp"].mean())

