
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[3]:


df.head(3)


# In[4]:


df.shape


# In[5]:


loc00 = df.loc[0]


# In[7]:


print(loc00) ; type(loc00)


# In[8]:


df.loc[90:100]


# In[9]:


print(df.loc[99])


# In[10]:


df.tail(3)


# In[11]:


print(df.loc[-1]) # -1과 같이 인덱스에 없는 값을 사용하면 오류가 발생.


# In[12]:


len(df)

