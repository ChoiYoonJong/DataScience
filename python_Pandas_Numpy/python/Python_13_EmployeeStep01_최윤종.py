#Python_13_EmployeeStep01_최윤종.py

# 인사 관리 시스템
# 사번, 이름, 입사일, 급여
# 계약직, 정규직
# 사번 1번째
# T, T << 계약직
# R << 정규직
#


TName = ["구분","사원명","입사일","급여"]

empInfo = [
	['T160501',"캔디","2016-05-10"],
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]

empPayTable = [
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]
]


for a in range(0,len(empInfo)):





print("구분","\t","사원명","\t","입사일","\t","급여")
print("-"*50)




'''
for i in range(0,5):
	empInfo[i][0][0] = empInfo[i][0][0].upper()
'''		

### "%s,\t%s,%t, %(직종,이름,날짜,[날짜*돈]) 


'''
print("계약직","\t","캔디","\t","\t","2016-05-10","\t","2500")
print("정규직","\t","장미","\t","\t","2016-05-10","\t","2400")
print("계약직","\t","튤립","\t","\t","2016-08-15","\t","2700")
print("계약직","\t","포도","\t","\t","2016-08-22","\t","2530")
print("정규직","\t","사과","\t","\t","2016-08-30","\t","1800")



'''


		

### 음... 리스트에 직원을 구분 하고 그리고  %d or %s 로 뭔가 링크 하는거 같고... 

