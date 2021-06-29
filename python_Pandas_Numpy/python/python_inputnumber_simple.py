'''
a = int(input('a입력:')) # 제대로 숫자가 들어가서 연결되서 사칙연산 계산 결과가 잘 나오게 된다.
b = int(input('b입력:'))
c = int(input('c입력:'))

print(a,b,c,a+b+c)

a = input('a입력:') # int 를 입력 하지 않을시 입력되는것이 문자형식으로 받아들여진다.
b = input('b입력:')
c = input('c입력:')

print(a,b,c,a+b+c)

a,b,c = map(int,input('a,b,c 값 입력 ex) 1 2 3').split()) #split() = 문자를 나뉘게 해준다. split() 앞에는 .을 써야한다.

print(a,b,c,a+b+c)
'''
text = input('날짜입력 yyyy.mm.dd')
y,m,d=text.split('.')

print(text,y,m,d)