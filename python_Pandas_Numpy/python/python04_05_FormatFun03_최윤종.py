#python04_05_FormatFun03_최윤종.py

a ="{2:<10}".format('aa', 'bb', 'cc')
b ="{1:>10}".format('aa','bb','cc')
c = "{:^10}".format('aa','bb','cc')
d="{:w^10}".format('aa', 'bb','cc')
print(a)
print(b)
print(c)
print(d)

x = 342134234
y = 3421.34235
e1= "{1:0.4f} {0:,d}".format(x,y)
e2= "{0:20.3f}".format(y)

print(e1)
print(e2)