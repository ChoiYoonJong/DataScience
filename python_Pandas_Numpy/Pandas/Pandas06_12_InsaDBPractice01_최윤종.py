
# coding: utf-8

# In[15]:


import pandas 


# In[25]:


deptDB = pandas.read_csv('../data/deptDB.csv',names=['deptno','dname','loc'], header=None)
sawonDB = pandas.read_csv('../data/sawonDB.csv', names=['sabun','saname','deptno','sajob','sapay'], header=None)
gogekDB = pandas.read_csv('../data/gogekDB.csv', names=['gobun','goname','gotel','gojumin','godam'], header=None)


# In[26]:


print(deptDB)
print("="*50)
print(sawonDB)
print("="*50)
print(gogekDB)
print("="*50)


# In[31]:


deptDB


# In[29]:


sawonDB


# In[30]:


gogekDB

