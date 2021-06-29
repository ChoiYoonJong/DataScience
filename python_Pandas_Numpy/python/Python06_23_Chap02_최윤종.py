#Python06_23_Chap02_최윤종.py

#Q1
hong = {'국어': 80, '영어': 75, '수학': 55}
average = sum(hong.values()) / len(hong)
print(average)

#Q2
a  = int(input("숫자를 입력하세요"))

if a % 2 == 0:
	print("짝수")
else:
	print("홀수")

#Q3
gil = "881120-1068234"
yyyymmdd = gil[:6]
num = gil[7:]
print(yyyymmdd)  
print(num)


#Q4
print("주민등록번호")
num = input("주민번호를 입력해주세요 : ")


birth_year = num[0:2]
birth_month = num[2:4]
birth_day = num[4:6]
sex = num[6]

if sex == '1' or sex == '3':
    sex = '남자'
elif sex == '2' or sex == '4':
    sex = '여자'
else:
    sex = '중성'

print("\n생년월일 : {0}년 {1}월 {2}일".format(birth_year, birth_month, birth_day))
print("성별 : {0}".format(sex))

#Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#Q6
a = [1, 3, 5, 4, 2]
a.sort( )
a.reverse( )
print(a) 

#Q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)



#Q8
a = (1, 2, 3)
a = a + (4,)
print(a)	