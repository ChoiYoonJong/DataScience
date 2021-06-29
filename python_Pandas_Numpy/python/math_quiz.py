import random # Random 숫자 관련 작업을 할때 맨처음으로 써야 적용이 된다.
import time # 시간의 관련되것을 작업할때 사용된다.

print("Welcome To")
print("!!! Math Quiz !!!")

playing = True
score = 0
count = 0

start_time = time.time()
while playing : # 이미 위에 True 가 있기 때문에 다시 쓸 필요가 없다.

	num1 =random.randint(1,9)
	num2 =random.randint(1,9)
	num3 =random.randint(1,9)

	answer = num1 * num2 - num3
	user_input = int(input(f"{num1} X {num2} - {num3} = "))
	count += 1

	if answer == user_input:
		score += 1
		print(f"정답입니다.현재 점수는{score}입니다.")
	else:
		playing = False
		print(f"아쉽네요. 정답은{answer}입니다.")

end_time = time.time()
print("="*50)
print(f" 총 {count}문제를 {round(end_time-start_time)}초만에 해결하셨습니다.")
print(f"현재 총 점수는{score}입니다.")
print("Math Quiz가 종료되었습니다.")