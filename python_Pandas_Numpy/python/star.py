count = int(input("열 갯수를 입력해 주세요: "))

for i in range(count,0,-1):
	for j in range(i):
		print("*",end=" ")
	print()