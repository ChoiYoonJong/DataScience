n = int(input("숫자를 입력해주세요:"))

is_prime = True
for i in range(2,n):
	if n%i ==0:
		is_prime = False
		break
if (is_prime):
	print(n, '은 소수입니다.')
else:
	print(n, '은 합성수입니다.')