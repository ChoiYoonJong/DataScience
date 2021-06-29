
# coding: utf-8

# In[7]:


import pandas as pd


# In[8]:


mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
df = pd.DataFrame(mydict)
df


# In[9]:


type(df.iloc[0])


# In[10]:


df.iloc[0]


# In[11]:


df.iloc[[0]]


# In[12]:


type(df.iloc[[0]])


# In[13]:


df.iloc[[0,1]]


# In[14]:


df.iloc[:3]


# In[15]:


df.iloc[[True,False,True]]


# In[16]:


df.iloc[0,1]


# In[18]:


df.iloc[[0,2],[1,3]]


# In[19]:


df.iloc[1:3, 0:3]


# In[20]:


df.iloc[:,[True,False,True,False]]

