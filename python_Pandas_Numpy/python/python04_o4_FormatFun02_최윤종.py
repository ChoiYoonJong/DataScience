#python04_04_FormatFun02_최윤종.py

a = "my name {}".format('Hong')
b = "{2} x {1} = {0}".format(11,2,11*2)
print(a)
print(b)

c = "{a} x {b} = {c}".format(a=11, b=2, c=11*2)
print(c)