
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np

deptDB = pd.read_csv('../data/deptDB.csv', header = None)
sawonDB=pd.read_csv('../data/sawonDB.csv', header = None)
geogekDB=pd.read_csv('../data/gogekDB.csv', header = None)

deptDB.columns =['deptno','dname','loc']

sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr']

geogekDB.columns=['gobun','goname','gotel','gojumin','godam']

deptDB = deptDB.replace("'","", regex=True)
sawonDB = sawonDB.replace("'","", regex=True)
geogekDB = geogekDB.replace("'","", regex=True)


# In[20]:


sawonDB


# In[21]:


q1_lst88 = []

for idx in range(len(sawonDB)):
    q1_lst88.append(sawonDB['sahire'][idx][1:5]=='1988')

print(q1_lst88)
sawonDB.loc[q1_lst88]

