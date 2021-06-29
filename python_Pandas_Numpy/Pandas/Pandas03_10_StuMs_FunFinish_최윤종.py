#Pandas03_10_StuMs_FunFinish_최윤종.py

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0

for i in range(len(idList)):
	dic[idList[i]] = scoreList[i]

def printList():
	print("="*100)
	for i in range(len(menu)):
		print(menu[i], end='\t')
	print()
	print("="*100)
printList()


while True:
	num = input("메뉴 번호를 입력하세요:")
	if num == "":
		print("번호 확인을 한번더 해주세요")
		continue
	
	if num in menuChk:
		if num == "9":
			print("메뉴종료")
			print(end='\t')
			break
		num = int(num)
		print("\t%s " %menu[int(num)-1])
		if num == 1:
			pass
		if num == 2:
			pass
		if num == 3:
			for i in range(len(MenuList)):
				print(MenuList[i],end="\t")
			print()
			print("="*100)
			for i in dic.keys():
				print(f"{i}\t{dic[i][0]}\t{dic[i][1]}\t{dic[i][2]}\t{sum(dic[i])}\t{sum(dic[i])/3:<.2f}",end="\t")
				print("합격" if sum(dic[i]) >=180 else "불합격")
			print("-"*60)
		
	else:
		print("다시확인해주세요")
