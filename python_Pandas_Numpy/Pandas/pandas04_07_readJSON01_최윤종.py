
# coding: utf-8

# In[1]:


import pandas as pd

#read_jsaon() 함수로 데이터프레임 변환
df = pd.read_json('./../DataSet/read_json_sample.json')
print(df, '\n')

print(df.index)

