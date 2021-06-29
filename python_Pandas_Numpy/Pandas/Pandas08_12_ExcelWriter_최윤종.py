
# coding: utf-8

# In[4]:


import pandas as pd 

data = {'name':['Jerry','Riah','Paul'],
       'algol':["A","A+","B"],
       'basic':["C","B","B+"],
       'c++':["B+","C","C+"]
       }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_json("./df_sample.json")


# In[5]:


import pandas as pd 

data = {'name':['Jerry','Riah','Paul'],
       'algol':["A","A+","B"],
       'basic':["C","B","B+"],
       'c++':["B+","C","C+"]
       }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_excel("./df_sample.xlsx")


# In[6]:


import pandas as pd

data1 = {'name':['Jerry','Riah','Paul'],
       'algol':["A","A+","B"],
       'basic':["C","B","B+"],
       'c++':["B+","C","C+"]}

data2 = {'c0':[1,2,3],
       'c1':[4,5,6],
       'c2':[7,8,9],
       'c3':[10,11,12],
        'c4':[13,14,15]}

df1 =pd.DataFrame(data1)
df1.set_index('name',inplace=True)
print(df1)
print('\n')

df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)
print(df2)

writer = pd.ExcelWriter("./df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name="시트1")
df2.to_excel(writer, sheet_name="시트2")
writer.save()

