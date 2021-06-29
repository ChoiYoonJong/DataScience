
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[ ]:


uniList = df['year'].unique()
print(type(uniList))
print(uniList, "")


# In[6]:


uniList = df['year'].unique()
print(type(uniList))
print(uniList,"\n====>")


# In[9]:


for idx in uniList:
    yearList = df[df["year"] == idx]
    print(len(yearList), "\n ====> 2 \n:", yearList.head(3), "n =====> 3 :", yearList.shape)
print(yearList["pop"].mean())


# In[10]:


grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df["pop"])


# In[11]:


grouped_year_df["pop"].mean()


# In[12]:


uniList = df['year'].unique()
for idx in uniList:
    print(idx, "======> 1 :")
    grYear =df[df['year']==idx]
    print(grYear['pop'].mean())

