#SET=2 Write A Python Program to Add the digits of the numbers.(Reverse it also)

number=int(input("Enter the Number ="))
print()

rev=0

copynumber=number
copynumber2=number

while number != 0:
	rem = number % 10
	rev = rev * 10 + rem
	number = number // 10

print("The Reverse, ",copynumber,"=",rev)

sum=0
while copynumber2 != 0:
	rem = copynumber2 % 10
	sum = sum + rem
	copynumber2 = copynumber2 // 10

print("The sum of digits of no, ",copynumber,"=",sum)