#Python04_11_strFunEx01QueryString_최윤종.py

'''
URL
QueryString
where=nexearch
sm=top_hty
fbm=1
ie=utf8
query=python

QueryString 개수: 5개
'''



a = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python"
URL=a.split("?")
print(URL[0])
print(URL[1])

b = URL[1].split("&")
print(b)


