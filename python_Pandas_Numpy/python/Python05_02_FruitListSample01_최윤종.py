#Python05_02_FruitListSample01_최윤종.py

A = 0
M = 0 
S = 0
G = 0

answer = []
fruitCnt = []

while True:
	num = int(input("10이상의 수를 입력하세요.[exit:0]>>>>"))
	if num >=10 :
		print("==<< %d번 반복합니다. >>==" %num)
		for i in range(1,num+1):
			if i % 3 == 0:
				answer.append("Apple")
			if i % 4 == 0:
				answer.append("Melon")
			if i % 5 == 0:
				answer.append("Grape")
			if i % 8 == 0:
				answer.append("StrawBerry")
			fruitCnt += answer
			

			if len(answer) == 0:
				print("%d." %i)
			else:
				print("%d." %i,str(answer))
			answer = []

		print("==<< Fruit Counter List >>==")
		print("Apple : %d회" %fruitCnt.count('Apple'))
		print("Melon : %d회" %fruitCnt.count('Melon'))
		print("Grape : %d회" %fruitCnt.count('Grape'))
		print("StrawBerry : %d회" %fruitCnt.count('strawBerry'))

	elif(num==0):
		print("^종료!!")
		bresk
	else:
		print("^10이상의 숫자를 확인하세요.")
		continue