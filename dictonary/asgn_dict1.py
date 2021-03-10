'''Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a product
name and print the corresponding price or a message if the product is not in the dictionary.'''

dicto={}
print("Enter how much products you want to add =")
no=int(input())


for i in range(no):

	'''it is given for the repetedly asking to user
	   enter the data'''
	no=int(input("The product no="))
	names=input("Enter the product name\t= ")
	price=input("Enter the price  value\t= ")
	print()
	dicto[no]={names:price}
	#print(type(dicto))...for checking the classs
	

	'''print("\nAre you want to enter(yes/no)=")
	choice=input()
	ch=choice.lower()

	if(ch!='yes'):
		break'''


print("\nThe Dictonary =\n")


for d,v in dicto.items():
	if d in dicto:
		print("\tThe product =",d,v)
	else:
		print("This product is not in dictonary")