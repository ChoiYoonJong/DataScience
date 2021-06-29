
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('../data/gapminder.tsv', sep='\t')


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[5]:


global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(type(global_yearly_life_expectancy))
print(global_yearly_life_expectancy)


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
global_yearly_life_expectancy.plot()


# In[7]:


plt.plot(global_yearly_life_expectancy,'ro')


# In[8]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()

