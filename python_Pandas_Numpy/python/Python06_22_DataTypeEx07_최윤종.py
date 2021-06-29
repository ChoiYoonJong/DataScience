#Python06_22_DataTypeEx07_최윤종.py
'''
다른 주소를 가리키도록 만들수는 없을까?

'''
a = [1,2,3]
b = a[:]
a[1]=4
print(a,"\t",b)

from copy import copy
a = [1,2,3]
b = copy(a)
print(b)
print(id(a))
print(id(b))