#Pandas02_04_FunEx09_최윤종.py
#함수 안에서 함수 밖의 변수를 변경하는 방법

# 1.return 사용하기
a=1
def vartest(a):
	a = a + 1
	return a

a = vartest(a)
print(a)
print("-"*20)
# 2. global 명령어 사용하기
# global 명령어: 함수 안에서 함수 밖의 변수를 직접 사용할때 사용. 권장X
# 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다.
a = 1
def vertest():
	global a
	a = a + 1

vertest()
print(a)