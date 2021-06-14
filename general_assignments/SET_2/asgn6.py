#SET 2=Write A Python Program to Find the Factorial of a Number

no=int(input("Enter the number "))

i=1
fact=1

while i <= no :
	
	fact=fact*i
	i=i+1

print("The Factorial of number",no,"=",fact)

