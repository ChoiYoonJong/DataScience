
# coding: utf-8

# In[1]:


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


# In[2]:


sajobChk = sawonDB[(sawonDB['sajob']=='대리') | (sawonDB['sajob']=='사원')]
sajobChk


# In[14]:


q9_job_meanpay = sawonDB['sajob'].unique()

a = sawonDB.groupby('sajob')['sapay'].count()
print(q9_job_meanpay)
for idx in q9_job_meanpay:
    payMeanlist = []
    chk = sawonDB[sawonDB['sajob'] == idx]
    if sawonDB.groupby('sajob')['sapay'].count()[idx] >=4:
        if idx == '사원':
            chkAll = sawonDB[sawonDB['sajob'] == idx]
            print("%s님들의 평균 급여는 %.2f 입니다." %(idx,chkAll['sapay'].mean()))
        elif idx == '대리':
            chkAll = sawonDB[sawonDB['sajob'] == idx]
            print("%s님들의 평균 급여는 %.2f 입니다." %(idx,chkAll['sapay'].mean()))

