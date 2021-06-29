print("!!구구단 출력 프로그램!!")

app_off ="아니요"
while app_off =="아니요":

	num = int(input("구구단 몇단을 출력해 드릴까여? >>>"))

	for i in range(1,10):
		print(f"{num} x{i} = {num*i} ")

	app_off = input("프로그램을 종료하시겠습니까? 네 / 아니요 >>>")
	print("="*50)
print("프로그램이 종료되었습니다.")