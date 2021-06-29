'''
input() 함수 이용
결과 : 4인 이상의 이름을 입력하세요.(SB 로 구분한다): 보라돌이 나나
- 4인이 아니면 ==> ^명수를 확인 하세요 (4인 이상)
- 4인 이상이라면 ==> 보라돌이 나나 뚜비 뽀오 입력 되었습니다...
'''
while True:
	
	a= input("4인 이상의 이름을 입력하세요 : ").split()

	if len(a) < 4:
		print("^\t명수를 확인하세요.")
		continue
	else:
		for i in a:
			print(i,end='')
		print("\t입력되었습니다.")
		