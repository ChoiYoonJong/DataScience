
# coding: utf-8

# In[35]:


import pandas as pd
# sheet_name ="시트1"
# header = None

df1 = pd.read_excel('./../DataSet/datalabPractice01.xlsx')
# 이렇게 쓰면 맨처음에 나오는 개요를 표시하려고 하는거다.

df2 = pd.read_excel('./../DataSet/datalabPractice01.xlsx',                    sheet_name = "Sheet1", usecols=[0,1,2], skiprows=[1],                    skipfooter =5, header =None )

# \ 의 의미는 가독성을 위해 문장을 붙여져 있는것을 표현하기 위해 쓰인다.
# usecols = [] : 행에 있는 것을 숫자를 입력해서 뭐를 보여줄지 혹은 안보여줄지를 정할 수 있다. ex) [0,1,2]
# skiprows =[] : 열에 있는 것을 하나씩 없앨 수 있다.  ex ) [1,2,3]
# skipfooter = []  : 열에 밑에서부터 숫자만큼 제거한다. ex) [4]

# usecols=[0,1,2] ,skiprows=[1], skipfooter=1
#print(df1.iloc[[0,2][1,2]],"\n")

print(df2.columns,"\n")
print(df2,"\n")
print(df1)

