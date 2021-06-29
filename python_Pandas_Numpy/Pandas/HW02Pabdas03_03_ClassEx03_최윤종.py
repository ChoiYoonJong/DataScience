#HW02Pabdas03_03_ClassEx03_최윤종.py

class FourCal:
	def setdata(self,first,second):
		self.first = first
		self.second = second
	
	def sum(self):
		result = self.first + self.second
		return result
	
	def sub(self):
		result = self.first - self.second
		return result
	
	def mul(self):
		result = self.first * self.second
		return result
	
	def div(self):
		result = self.first / self.second
		return result

a = FourCal()
#FourCal.setdata(a,3,4)
a.setdata(3,4)