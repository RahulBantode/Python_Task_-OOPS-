'''Problem Statement :-
write a program which contains one lambda function which accepts two parameters and
return its multiplication '''

Multiplication = lambda number1,number2 : number1*number2

def main():
	number1 = int(input("Enter the 1st number : "))
	number2 = int(input("Enter the 2st number : "))

	mult = Multiplication(number1,number2)

	print("Multiplication of {}*{} : {}".format(number1,number2,mult))

if __name__ == '__main__':
	main()