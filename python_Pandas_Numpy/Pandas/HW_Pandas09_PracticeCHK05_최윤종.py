
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np

deptDB = pd.read_csv('../data/deptDB.csv', header = None)
sawonDB=pd.read_csv('../data/sawonDB.csv', header = None)
geogekDB=pd.read_csv('../data/gogekDB.csv', header = None)

deptDB.columns =['deptno','dname','loc']

sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr']

geogekDB.columns=['gobun','goname','gotel','gojumin','godam']


deptDB['dname'] = deptDB['dname'].str.strip("' '")
deptDB['loc'] = deptDB['loc'].str.strip("' '")

deptDB['dname'] = deptDB['dname'].str.strip()
deptDB['loc'] = deptDB['loc'].str.strip()


sawonDB['saname'] = sawonDB['saname'].str.strip("' '")
sawonDB['sajob'] = sawonDB['sajob'].str.strip("' '")
sawonDB['sahire'] = sawonDB['sahire'].str.strip("' '")
sawonDB['sasex'] = sawonDB['sasex'].str.strip("' '")

sawonDB['saname'] = sawonDB['saname'].str.strip()
sawonDB['sajob'] = sawonDB['sajob'].str.strip()
sawonDB['sahire'] = sawonDB['sahire'].str.strip()
sawonDB['sasex'] = sawonDB['sasex'].str.strip()

geogekDB['goname'] = geogekDB['goname'].str.strip("' '")
geogekDB['gotel'] = geogekDB['gotel'].str.strip("' '")
geogekDB['gojumin'] = geogekDB['gojumin'].str.strip("' '")

geogekDB['goname'] = geogekDB['goname'].str.strip()
geogekDB['gotel'] = geogekDB['gotel'].str.strip()
geogekDB['gojumin'] = geogekDB['gojumin'].str.strip()


# In[11]:


sawonDB.head()


# In[15]:


q1_lst88 = []

for idx in range(len(sawonDB)):
    q1_lst88.append(sawonDB['sahire'][idx][0:4]=='1988')

print(q1_lst88)
sawonDB.loc[q1_lst88]


# In[18]:


q3_sabun = sawonDB[sawonDB['sabun']%2 == 0]

q3_sabun

