# Python02_15_AutoMachine_step02_최윤종.py

menu =['오렌지','딸기',

print("**** 홍익대학교 과일 판매머신 V02 *****")
print("1.오렌지:2400원")
print("2.딸기:3000원")
print("3.망고:4000원")
print("4.복숭아:5000원")
print("5.포도:6000원")
print("6.종료")
print("============================")

while True:
	number = input("구매번호를 입력하세요 : ")
	num = int(number)
	if num == 1:
		print("오렌지는 2400원입니다.")
	elif num == 2:
		print("딸기는 3000원입니다.")
	elif num == 3:
		print("망고는 4000원입니다.")
	elif num == 4:
		print("복숭아는 5000원입니다.")
	elif num == 5:
		print("포도는 6000원입니다.")
	else:

