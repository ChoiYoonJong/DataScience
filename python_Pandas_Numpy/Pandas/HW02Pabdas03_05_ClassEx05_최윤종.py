#HW02Pabdas03_05_ClassEx05_최윤종.py

class FourCal:
	def __init__(self):
		pass
	def __init__(self,first,second):
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
	
class MoreFourCal(FourCal):
	def pow(self,su01):
		result = su01**2
		return result


a=MoreFourCal(4,2)