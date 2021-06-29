import sys
import random

while True:
    a=[]
    b=[]

    a = input("4인 이상의 이름을 입력하세요.(종료:0):").split()
    if '0' in a:
        sys.exit()

    if len(a) <4:
        print("\t명수를 확인하세요.")
        continue
    else:
        while True:
            num = random.randint(1,len(a))
            if num not in b:
                b.append(num)
            else:
                continue

            if len(b) == len(a):
                break
        for i in a:
            print(i,end=' ')
        print('이고')
        for i in b:
            print(i,end=' ')
        print("입니다.") 
    
