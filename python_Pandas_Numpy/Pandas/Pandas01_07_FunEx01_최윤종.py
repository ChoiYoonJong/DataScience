
# coding: utf-8

# ### 기본 함수 선언 연습 01
# <h1> 기본 연습 </h1>
# <h2> 기본 연습 </h2>
# <h3> 기본 연습 </h3>
# <h4> 기본 연습 </h4>
# <h5> 기본 연습 </h5>
# HTML : Hyper Text Markup Language
#                                             <,>,/

# In[4]:


def add(a,b):
    return a+b

a=3
b=4
c=add(a,b)

print("%d+%d = %d" %(a,b,c))


# In[5]:


#1. 일반적인 함수
def add(a,b): #a,b는 매개변수
    return a,b,a+b

a,b,result = add(b=5,a=3)
print("%d+%d = %d" %(b,a,result))
print("-"*20)


# In[6]:


#2.입력값이 없는 함수
def say():
    return'Hi'

print(say())
print("-"*20)


# In[7]:


#3. 결과 값이 없는 함수
#결과 값은 오직 return 명령어로만 돌려받을 수 있다.

def add2(a,b):
    print("%d,%d의 합은 %d입니다." %(a,b,a+b))
    
print(add2(3,4))
print("-"*20)


# In[8]:


#4.입력값도 결과 값도 없는 함수
def say2():
    print('Hi')

say2()
print("-"*20)

