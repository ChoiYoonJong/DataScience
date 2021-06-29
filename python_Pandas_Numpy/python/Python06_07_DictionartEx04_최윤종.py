#Python06_07_DictionartEx04_최윤종.py
'''
딕셔너리 관련 함수들
Keys 리스트 만들기(Keys)
'''

a = {'name':'prey','phone':'0119993323','birth':'1118'}
print(a.keys())

'''
dict_keys, dict_values, dict_items등은 리스트로 변환하지 않더라고 기본적인 
반복(interate)구문(예:for문)을 실행할 수 있다.
'''

for k in a.keys():
	print(k)

print("-"*15)
#dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
vList = list(a.keys())
print(vList)
print("-"*15)