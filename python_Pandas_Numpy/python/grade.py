marks = [ 50, 60, 70, 80, 90]

number = 0
for mark in marks:
	number = number + 1 
	if mark >= 60:
		print (number, "번 학생은 합격입니다.")
	else:
		print(number, "번 학생은 불합격입니다.")