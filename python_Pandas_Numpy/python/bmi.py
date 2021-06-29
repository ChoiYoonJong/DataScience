print("="*50)
print("\t체질량 지수BMI를 확인하세요")
print("="*50)
print()

height = float(input("키를 입력하세요(단위: 미터) >>>"))
weight = float(input("몸무게를 입력하세요 >>>")) # 숫자가 소수일때 int 가 아닌 float 라는 함수를 사용한다.
bmi_chk = "ㅇ"

bmi = round(weight / height **2,1) # round 는 반올림을 할때 쓰는 함수이다. 
print(bmi)

print()
print("+"*20)
print("BMI결과")
if bmi < 18.5:
	print(bmi_chk)
	print("저체중입니다.")

elif bmi < 25:
	print(bmi_chk*2)
	print("정상입니다.")

elif bmi < 30:
	print(bmi_chk*3)
	print("경도비만입니다.")

elif bmi < 35:
	print(bmi_chk*4)
	print("경도비만입니다.")

else:
	print(bmi_chk*5)
	print("고도비만입니다.")
print("+"*20)