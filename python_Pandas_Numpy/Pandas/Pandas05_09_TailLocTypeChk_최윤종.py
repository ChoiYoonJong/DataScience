
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep ='\t')


# In[3]:


df.head(2)


# In[11]:


subset_loc = df.loc[0]
subset_tail = df.tail(1)
subset_head = df.head(1)

print(subset_loc, "\n===>")
print(subset_tail, "\n")

print(type(subset_loc))
print(type(subset_tail))
print(type(subset_head))

