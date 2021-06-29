user_input = input("!!잠금!! 비밀번호를 입력해주세요 >>>>>")
while user_input != 'A1234':
	print("wrong password")
	user_input = input("잘못된 비밀번호입니다.다시입력해주세요>>>")

print("!! 잠금이 해제되었습니다.!!")