#python03_08_ForExp00_최윤종.py


a = [1,2,3,4]     #표현식 if 조건 else 
result =[]
for num in a:
	result.append(num*3)

print(result)

print("="*50)


result = [num*3 for num in a]
print(result)

#[3,6,9,12]