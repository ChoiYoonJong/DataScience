
# coding: utf-8

# In[2]:


def add_mul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i  # i 만큼 더한것을 축적하는거
    elif choice == "mul":
        result = 1
        for i in args:
            result = result *i  # i 만큼 곱하는것을 축적...
    return result
    
result1 = add_mul('add',2,3)
print(result1)
print("-"*20)
result2 = add_mul('mul',2,3)
print(result2)

