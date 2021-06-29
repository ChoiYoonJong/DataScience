
# coding: utf-8

# In[3]:


import pandas as pd

student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1, '\n')

percentage = student1 / 200

print(percentage, '\n')
print(type(percentage))


# In[6]:


import pandas as pd

student1 = pd.Series({'국어':100,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90,'영어':80})

print(student1, '\n')
print(student2, '\n')

addition = student1 + student2
subtraction = student1 - student2
multipication = student1 * student2
division =student1 / student2
print(type(division),'\n')

result = pd.DataFrame([addition,subtraction,multipication,division],
                     index=['덧셈','뺄셈','곱셈','나누기'])
print(result,"\n", type(result))
print(addition, "\n", subtraction, "\n", multipication, "\n", division)

