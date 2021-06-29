
# coding: utf-8

# In[25]:


import pandas


# In[36]:


df = pandas.read_csv('../data/gapminder.tsv',sep='\t')


# In[63]:


uniList_year = df["year"].unique()
uniList_continent = df["continent"].unique()
uniList_continent.sort()
uniList_year.sort()
print("-"*60)
for i in uniList_year:
    Chk01 = df[df["year"]==i]
    for j in uniList_continent:
        Chk02 = Chk01[df["continent"]==j]
        print(f"{i}년 {j:^10}지역의 기대수명 평균{Chk02['lifeExp'].mean():.2f}")
    print("-"*60)

