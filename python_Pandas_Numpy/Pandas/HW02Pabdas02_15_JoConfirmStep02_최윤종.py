# HW02Pabdas02_15_JoConfirmStep02_최윤종.py

'''
조건)
- 4인 이상 len() 인원수 반환
- 5명 -> 1~5
- 중복 없이 반환
'''

import random

while True:
	
	a= input("4인 이상의 이름을 입력하세요 : ").split()

	if len(a) < 4:
		print("^\t명수를 확인하세요.")
		continue
	else:
		for i in a:
			print(i,end='')
		print("\t입력되었습니다.")
		break
