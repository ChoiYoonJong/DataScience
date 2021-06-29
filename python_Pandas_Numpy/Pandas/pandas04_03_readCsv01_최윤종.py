
# coding: utf-8

# In[20]:


import pandas as pd

file_path = './../DataSet/read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1, '\n')
print(type(df1))

