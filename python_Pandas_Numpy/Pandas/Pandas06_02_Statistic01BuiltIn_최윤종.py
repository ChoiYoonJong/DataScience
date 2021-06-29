
# coding: utf-8

# In[1]:


import numpy as np


# In[9]:


dataList = [28,31,24,25,30,32,20,30,31,26,31]


import pandas as pd

da = pd.Series(dataList)

print("Built-in 정렬 sort_values() : \n",da.sort_values(ascending=True))
print("="*100)
print("Built-in 평균 mean() : %d" %da.mean())
print("="*100)
print("Built-in 중위수 median() : %d" %da.median())
print("="*100)
print("Built-in 분산 var() : %d" %da.var())
print("="*100)
print("Built-in 표준편차 std() : %d" %da.std())
print("="*100)
print("Built-in 제1사분위수 quantile() : %d" %da.quantile(q=0.25))
print("="*100)
print("Built-in 제2사분위수 quantile() : %d" %da.quantile(q=0.5))
print("="*100)
print("Built-in 제3사분위수 quantile() : %d" %da.quantile(q=0.75))
print("="*100)
da.describe()

