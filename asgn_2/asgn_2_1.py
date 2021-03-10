''' statement :- create a module named as Arithmetic which contains 4 functions as Add(),Sub(),Mult(),Div()
				 All functions accepts two parameters as number and perform the operation. Write a python 
				 program which call all the functions from Arithmetic module by accepting the para.
				 from user
'''

from arithmetic import *

def main():
	no_1 = int(input("Enter the 1st number : "))
	no_2 = int(input("Enter the 2nd number : "))


	ans = Add(no_1,no_2)
	print("Addition is : ",ans)

	ans = Sub(no_1,no_2)
	print("Substraction is : ",ans)

	ans = Mult(no_1,no_2)
	print("Multiplication is : ",ans)

	ans = Div(no_1,no_2)
	print("Division is : ",ans)

	

if __name__ == '__main__':
	main()