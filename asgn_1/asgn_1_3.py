'''statement :- Write a program which contains one function named as Add() which accepts two numbers
				from user and return addition of the two numbers 
'''

def Add(value_1,value_2):
	return value_1 + value_2

def main():
	no_1 = int(input("Enter the 1st number : "))
	no_2 = int(input("Enter the 2nd number : "))

	ans_addition = Add(no_1,no_2)

	print("Addition : {}+{} = {}".format(no_1,no_2,ans_addition))

if __name__ == '__main__':
	main()
