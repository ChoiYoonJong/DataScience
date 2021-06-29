
# coding: utf-8

# In[1]:


import pandas 


# In[2]:


deptDB = pandas.read_csv('../data/deptDB.csv',names=['deptno','dname','loc'],header=None,delimiter= ",")
sawonDB = pandas.read_csv('../data/sawonDB.csv', names=['sabun','saname','deptno','sajob','sapay'], header=None)
gogekDB = pandas.read_csv('../data/gogekDB.csv', names=['gobun','goname','gotel','gojumin','godam'], header=None)


# In[3]:


deptDB = deptDB.replace('\'','',regex=True)


# In[4]:


deptDB


# In[5]:


sawonDB = sawonDB.replace('\'','',regex=True)


# In[6]:


sawonDB
# 88년생 사원 출력
#4월 입사한 사월 출력
#사원번호가 짝수인 사람
#직위별 급여 평균
#직위별 성별 평균


# In[49]:


uniYear = sawonDB['deptno'].unique()

print(uniYear[i][0:5])

# 88년생 사원 출력
#4월 입사한 사월 출력
#사원번호가 짝수인 사람
#직위별 급여 평균
#직위별 성별 평균


# In[7]:


gogekDB = gogekDB.replace('\'','',regex=True)


# In[8]:


gogekDB

