# Python02_20_AutoMachine_step05_최윤종.py

menu =['오렌지','딸기','복숭아','망고','포도','종료']
money=[1000,2500,1500,2000,2000]

print("**** 홍익대학교 과일 판매머신 V03 *****")

for num in range(0,5):
	print(num+1,"번",menu[num],":",money[num],"원")

print("==================================")

while True:
	n= input("구매번호를 입력하세요.(1~6):")
	n= int(n)
	m= input("코인을 투입하세요. : ")
	m= int(m)
	if n in range(1,7):
		print(menu[n-1],"는",money[n-1],"원 입니다.")
	if m >= money[n-1]:
		print("받은 금액 :" ,m,"원")
		print("거스름돈은 :",m-money[n-1],"원 입니다.")
		print("=========================")
	else:
		print(money[n-1]-m,"원 이 부족합니다.")
		print("=========================")

	
		



'''
	if n ==1:
		print(menu[n-1],"는", money[n-1],"원 입니다.")
		print("==========================")
	elif n ==2:
		print(menu[n-1],"는", money[n-1],"원 입니다.")
		print("==========================")
	elif n ==3:
		print(menu[n-1],"는", money[n-1],"원 입니다.")
		print("==========================")
	elif n ==4:
		print(menu[n-1],"는",money[n-1],"원 입니다.")
		print("===========================")
	elif n ==5:
		print(menu[n-1],"는",money[n-1],"원 입니다.")
		print("============================")
	else:
		print("종료")
	print("=============================")
	break
'''