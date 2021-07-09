#Python05_15_MemberStep02Ins_최윤종.py

#data
menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']





print("="*20,"메뉴선택","="*20)

for aaa in range(len(menu)):
	print(menu[aaa],end=' ')
print()

print("="*50)




while True:
	num = int(input("메뉴의 번호를 입력해주세요 : "))
	if num == 1:
		for B in range(len(itemList)):
			input(itemList[B])
	elif num == 2:

		

		

# input 글 쓰고... 연결 후////  print(  %d ...) 
