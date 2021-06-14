#SET2=Write A Python Program to Check Armstrong Number

number=int(input("Enter the number ="))

copyno=number
rem=0
summ=0
while number != 0:
	rem=number % 10
	summ=summ + rem*rem*rem
	number=number//10


if summ == copyno:
	print("The no ",copyno,"is Armstrong number ")
else:
	print("The no ",copyno,"is not Armstrong number ")

'''Firstly i type like number=number/10
because it gives result in fraction point thats why
my answer is getting wrong to resolve this problem
i use number=number//10 which gives an floor division
'''