#Pandas02_01_FunEx06_최윤종.py
# 두번째 return문인 return a*b는 실행되지 않았다
def add_and_mul(a,b):
	return a+b
	return a*b

result = add_and_mul(2,3)
print(result)
print("-"*10)

#[return의 또다른 쓰임새]
#return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.

def say_nick(nick):
	if nick =="바보":
		return
	print("나의 별명은 %s입니다." %nick)

say_nick('야호')
say_nick('바보')
print("-"*10)