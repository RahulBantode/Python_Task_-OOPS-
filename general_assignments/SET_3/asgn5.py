#5.	Write A Python Program to calculate the square of the given number using math function

def square(no):
	result=no*no
	return result


enter_no=int(input("Enter the number = "))
result=square(enter_no)

print("The square of ",enter_no,"=",result)