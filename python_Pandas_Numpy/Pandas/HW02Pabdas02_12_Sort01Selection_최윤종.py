#HW02Pabdas02_12_Sort01Selection_최윤종.py

num = [2,5,6,1,2,8,33,77,12]

for i in range(len(num)-1):
	for j in range(i+1,len(num)):
		if(num[i]>num[j]):
			num[i],num[j] = num[j],num[i]
print([num])