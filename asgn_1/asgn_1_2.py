'''statement :- write a program which contains one function named as CheckNum() which accept one parameter as
				number. If number is even then it should display "Even Number" otherwise display
				"odd number" on console
'''

def CheckNum(value):
	if value % 2 == 0:
		return True
	else:
		return False

def main():
	value = int(input("Enter one number : "))

	answer = CheckNum(value)

	if answer == True:
		print("{} number is even".format(value))
	else:
		print("{} number is odd".format(value))

if __name__ == '__main__':
	main()