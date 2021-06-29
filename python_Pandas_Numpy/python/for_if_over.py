#for + if 
'''
n=int(input('n:'))
for i in range(1,n+1):
	if i%3 ==0: # i 의 값이 3으로 나누었을때 나머지가 0인견우 , 3의배수
		print('X')
	else:
		print(i)
		'''
'''
#while + if
num1 = 0
num2 = int(input('n:'))

while True: #무한 루프상태 , 실행을 하게되면 1씩 늘어나는거...
	num1 = num1 + 1
	print(num1)
	if num1== num2: #num1 에 1씩 추가 되면서 나중에 num2와 num1 이 같아지게되면 멈추는공식
		break	
		'''

#for + for

'''
for i in range(1,7):
	for j in range(1,7):
		print(i,j)
'''