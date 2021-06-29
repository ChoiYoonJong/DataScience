
# coding: utf-8

# In[6]:


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


# In[14]:


sajobChk = sawonDB[:][(sawonDB['sajob']=='대리') | (sawonDB['sajob']=='사원')]
sajobCntChk = sajobChk.groupby(['sajob'])['sabun'].count() >=4

sajobChkResult = sajobCntChk[sajobCntChk.values]

for i, value in enumerate(sajobChkResult.index):
    cal = sawonDB[sawonDB['sajob']== value]
    print(cal.groupby('sajob')['sapay'].mean())


# In[17]:


sajobChk.groupby(['sajob'])['sabun'].count()


# In[18]:


sajobChk.groupby(['sajob'])['sabun'].count() >= 4


# In[20]:


(sajobChk.groupby(['sajob'])['sabun'])


# In[21]:


sajobCntChk = (sajobChk.groupby(['sajob'])['sabun'].count() >=4)
sajobCntChk

