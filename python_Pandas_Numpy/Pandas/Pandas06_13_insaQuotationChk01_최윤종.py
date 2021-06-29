
# coding: utf-8

# In[20]:


import pandas as pd


# In[21]:


deptDB = pandas.read_csv('../data/deptDB.csv',names=['deptno','dname','loc'],header=None,delimiter= ",")
sawonDB = pandas.read_csv('../data/sawonDB.csv', names=['sabun','saname','deptno','sajob','sapay'], header=None)
gogekDB = pandas.read_csv('../data/gogekDB.csv', names=['gobun','goname','gotel','gojumin','godam'], header=None)


# In[27]:


deptDB = deptDB.replace('\'','',regex=True)


# In[28]:


deptDB


# In[29]:


sawonDB = sawonDB.replace('\'','',regex=True)


# In[30]:


sawonDB


# In[31]:


gogekDB = gogekDB.replace('\'','',regex=True)


# In[32]:


gogekDB

