#python03_06_GuGuDaneX03_최윤종.py

'''for 문: 반복문
다중 for문..2중

for문안에 for문

outer for <<< 1회
	inner for

'''

for i in range(2,4):
	print("outer:",i)
	for j in range(1,4):
		print("inner:",j,end=' ')
	print("")