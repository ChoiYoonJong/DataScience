
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.columns,"\n", titanic.shape)
df = titanic.loc[:,['age','fare']]
print(df.head(),'\n')
print(type(df),'\n')

addition = df + 10
print(addition.head(),'\n')
print(type(addition))


# In[2]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.tail(),'\n')
print(type(df), '\n', df.shape)

addition = df + 10
print(addition.tail(),'\n')
print(type(addition),'\n')

subtraction = addition - df
print(subtraction.tail(), '\n')
print(type(subtraction))

