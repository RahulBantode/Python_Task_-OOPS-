'''Problem Statement :- WAP which accept number from user and return its factorial 
input - 5
output- 120
'''
fact = 1
i = 1
def Factorial(no):
	global fact,i

	if i <= no:
		fact = fact * i
		i = i + 1	
		Factorial(no)

	return fact

def main():
	number = int(input("Enter the Number : "))

	fact = Factorial(number)

	print("Factorial of Number {} : {}".format(number,fact))


if __name__ == '__main__':
	main()
