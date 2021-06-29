
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[6]:


df.head(3)


# In[7]:


df.shape


# In[9]:


loc00 = df.loc[0]


# In[10]:


print(loc00) ; type(loc00)


# In[11]:


df.loc[90:100]


# In[12]:


print(df.loc[99])


# In[13]:


df.tail(3)


# In[14]:


len(df)


# In[16]:


number_of_rows = df.shape[0]
print(number_of_rows, "\n\n")

last_row_index = number_of_rows -1

print(df.loc[last_row_index])


# In[17]:


print(df.loc[len(df)-1])


# In[18]:


print(df.tail(n=1))


# In[19]:


print(df.tail(n=2))


# In[20]:


print(df.loc[[0,99,999]])

