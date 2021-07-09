#python03_09_ForExp02_최윤종.py

'''
print(10/3)
print(10%3)
print(10//3)
'''

a = [1,2,3,4]

result = [num * 3 for num in a if num % 2 ==0]

print(result)

'''
for num in a
	if num % 2 == 0
		num * 3
'''
