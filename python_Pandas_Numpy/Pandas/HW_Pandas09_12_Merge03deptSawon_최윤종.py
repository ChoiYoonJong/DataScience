
# coding: utf-8

# In[73]:


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


# In[78]:


deptSawon = deptDB.merge(sawonDB, how='inner', on='deptno')
deptSawon.head(20)


# In[79]:


q7_com_30 = sawonDB[sawonDB['deptno']==30]
print("전산부 직원의 평균 연봉 :",q7_com_30['sapay'].mean())

