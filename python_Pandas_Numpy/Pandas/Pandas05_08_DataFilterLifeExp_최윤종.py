
# coding: utf-8

# In[7]:


import pandas 


# In[8]:


s = pd.Series([4, 2, 0, 8])
print(s)
print(s.max())
print(s.min())

# 문제] 최대 기대 수명, 최소 기대 수명 출력
# [loc, iloc, 컬럼명 3가조 확인]


# In[10]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')
df


# In[45]:


life_exp = df.iloc[:,[3]]
life_exp


# In[46]:


print(life_exp.max())


# In[47]:


print(life_exp.min())


# In[48]:


life_exp2 = df.loc[:,['lifeExp']]


# In[49]:


life_exp2


# In[38]:


print(life_exp2.max())


# In[39]:


print(life_exp2.min())


# In[51]:


print(max(df.iloc[:len(df)+1, 3]))
print(min(df.iloc[:len(df)+1, 3]))

