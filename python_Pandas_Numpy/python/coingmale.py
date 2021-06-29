import random
print("재미있는 동전게임 플레이 하시는것을 환영합니다.")

computer = random.randint(0,1) # 컴퓨텀 가 숫자 랜덤 하는 역활 
choice = int(input("앞면일까요? 뒷면일까여? 0:앞면 , 1:뒷면 \n")) #내가 고른 번호 선택지를 누르고 그리고 n 은 엔터 역활 



print("동전결과")
if computer == 0:
	print("앞면")
else:
	print("뒷면")

print("나의 선택")
if choice ==0:
	print("앞면")
else:
	print("뒷면")

print("게임 결과")
if choice == computer:
	print("축하합니다동전의 면의 위치를 정확하게 맞추었습니다")
else:
	print("적중하는것에 실패하였습니다.")