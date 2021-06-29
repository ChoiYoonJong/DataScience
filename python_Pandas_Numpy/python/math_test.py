# {:.numf} - {}안에 ":" + ".숫자" + "f" 를 작성시 소수점을 자기가 원하는 숫자 길이만큼 설정해서 나오게 할 수 있다.

'''
a1 = 10.103
b1 = 20.312
print('{} x {:.3f} = {:.3f}'.format(a1,b1,a1*b1)) # 소수점 3개까지 나오게 할 수 있다.

'''
'''
yard = 91.44
inch = 2.54

n1 = 2.1
n2 = 10.5

print('{:4}yd = {:5.1f}cm'.format(n1,n1*yard)) # {:4}를 넣은 의미는 정수에 결과가 4자리로 만들때 그러므로 앞에 공간이 나온다.
print('{:4}inch = {:5.1f}cm'.format(n2,n2*inch))
'''
'''
height = int(input('height='))

print('Your height is {}cm'.format(height))
'''
'''
n1,n2 = map(int,input().split())
print(n1)
print(n2)
'''
'''
f1 = float(input())
f2 = float(input())
f3 = float(input())

print(round(f1,3)) # round 라는 것은 반올림 역활로 작용한다 그리고 그뒤에 숫자를 넣음으로써 소수점 수를 적용시킬 수 있다.
print(round(f2,3))
print(round(f3,3))
'''