
# coding: utf-8

# In[2]:


import pandas as pd
file_pathExcel = './../DataSet/datalabPractice01.xlsx'
dfExcel = pd.read_excel(file_pathExcel)
print(dfExcel)
print(type(dfExcel))

