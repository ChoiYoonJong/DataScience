#Python04_02_FruitListStep01_최윤종.py

A = 0
M = 0 
S = 0
G = 0

while True:
	num = int(input("10이상의 수를 입력하세요.[exit:0]>>>>"))
	if num >=10 :
		print("FruitList Alogiruthm Chk")
	elif(num==0):
		print("^종료!!")
		bresk
	else:
		print("^10이상의 숫자를 확인하세요.")
		continue