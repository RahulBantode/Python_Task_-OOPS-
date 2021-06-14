'''fibonaci series'''


a=0
b=1
no=int(input("Enter the no ="))

print("The fibonaci series are....")

#print(a)
#print(b)

i=0
while i<=no:
	if(i<=1):
		next=i
	else:
		next=a+b

	a=b
	b=next
	print(next,end="\t")
	i=i+1




	
