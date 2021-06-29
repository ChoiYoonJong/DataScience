
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[7]:


print(df.head(n=3))


# In[8]:


uniYear = df['year'].unique()
print(uniYear)


# In[9]:


print(df.groupby('year')['lifeExp'].mean())


# In[3]:


type(df)
print


# In[4]:


type(df['pop'])


# In[5]:


grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df["pop"])


# In[6]:


grouped_year_df["pop"].mean()

