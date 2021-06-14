#set1= 5.Write A Python Program to Convert Kilometers to Miles.

kilometer=int(input("Enter in the K.M ="))


result=0
k=kilometer
if kilometer==1:
	print("The result in miles =",0.621)
else:
	m=1
	while m<=kilometer:
		result=result+0.621
		m=m+1
	print("The result in miles =",result)



