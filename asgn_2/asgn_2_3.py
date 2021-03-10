'''statement : wap which accept one number and calculate factorial of that number '''

def CheckFact(no):
	i=1
	fact=1
	while i <= no:
		fact = fact * i
		i = i+1

	return fact

def main():
	value = int(input("Enter the number : "))

	factorial_ans = CheckFact(value)

	print("Factorial of {} : {}".format(value,factorial_ans))

if __name__ == '__main__':
	main()
