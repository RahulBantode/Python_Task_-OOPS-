#set 2=Write A Python program to check if a number is positive, negative or zero

number=int(input("Enter the Number = "))

if number < 0:
	print("The number",number,"is negative")
elif number ==0:
	print("The number",number,"is zero")
else:
	print("The number",number,"is positive")

