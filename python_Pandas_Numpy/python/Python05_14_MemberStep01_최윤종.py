#Python05_14_MemberStep01_최윤종.py

'''
menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']
'''

print("="*20,"메뉴선택","="*20)
print('1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료')
print("="*50)

while True:
	user_input = input("메뉴의 번호를 선택해주세요 :")

	if(user_input ==""):
		print("Chk")
	
	elif(user_input =="1"):
		print("1.회원가입")
	elif(user_input =="2"):
		print("2.로그인")
	elif(user_input =="3"):
		print("3.회원목록")
	elif(user_input =="9"):
		print("9.메뉴종료")
		break
	


	


## n = int(input("메뉴의 번호를 선택해주세요. : "))






### 메뉴 번호 선택 해주세요... 회원 가입 해주세요... 메뉴 번호 로그린 휘원 목록 메뉴 번호 종류.....
