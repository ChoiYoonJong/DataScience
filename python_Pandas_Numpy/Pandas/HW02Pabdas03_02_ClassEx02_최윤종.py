#HW02Pabdas03_02_ClassEx02_최윤종.py

class FourCal:
	def setdata(self,first,second):
		self.first = first
		self.second = second
a = FourCal()


FourCal.setdata(a,2,3)

print(a.first,a.second)
a.setdata(4,5)
print(a.first,a.second)

