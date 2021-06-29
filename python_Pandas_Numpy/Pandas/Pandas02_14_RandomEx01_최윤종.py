#Pandas02_14_RandomEx01_최윤종.py

import random

for i in range(5): # i = 1,2,3,4,5
	print("%f" %random.random(),end=' ')

print("\n", "-"*50, "\n")

for i in range(5):
	print("%d" %random.randint(1,3),end=' ')

print("\n", "-"*50, "\n")

for i in range(5):
	print("%d" %random.randint(1,45),end=' ')
print()