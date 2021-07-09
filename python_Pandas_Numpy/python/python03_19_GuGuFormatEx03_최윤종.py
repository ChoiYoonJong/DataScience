# python03_19_GuGuFormatEx03_최윤종.py

for i in range(2,10):
	print("# %단" % i, end=" ")
print("\n\n")
print("="*70)

for i in range(2,10):        
   for j in range(2,10):   
       print("%dx%d=%d" %(j,i,j*i),end ="")
   print('\n\n') 

print("-"*70)

 