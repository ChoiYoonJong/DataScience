'''
#for 변수 in range(시작<이상>,끝<미만>):

for i in range(1,3): # 1,2
	print(i)
'''

#1~100 까지의 합

sum_100 = 0

for i in range(1,101):
	sum_100 += i 

print(sum_100)

# 1~100까지의 짝수의합

sum_even = 0
for i in range(2,101,2):# 마지막 3번째는 2만큰 증가해서 값이 오른다 # 2,4,6,8 ...
	sum_even += i

print(f"1부터 100까지의 짝수의 합 : {sum_even}")
