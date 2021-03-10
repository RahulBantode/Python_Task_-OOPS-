''' statement : write a program which contains one function that accept one number from user
				and returns true if number is divisible by 5 otherwise return false'''


def DivisibleBy(value):
	if value % 5 == 0:
		return True 
	else:
		return False

def main():
	no = int(input("Enter the number : "))

	answer = DivisibleBy(no)

	if answer == True:
		print("True : Number {} is divisible by 5".format(no))
	else:
		print("False : Number {} is not divisible by 5".format(no))

if __name__ == '__main__':
	main()