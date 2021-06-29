
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')
print(df)


# In[3]:


# 데이터의 자료형을 확인
type(df)


# In[4]:


# 데이터프레임의 열 확인
print(df.columns)


# In[5]:


# 데이터프레일의 행 확인
df.index


# In[6]:


# 데이터프레임을 구성하는 값의 자료형을 확인
print(df.dtypes)


# In[7]:


# 데이터 잡합과 각 열들의 자료형을 자세히 확인
print(df.info())


# In[8]:


# 에서는 (행, 열) 크기를 알 수 있습니다.
df.shape

