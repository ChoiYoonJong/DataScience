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
	cash = int(input("돈을 넣어주세요 :")
