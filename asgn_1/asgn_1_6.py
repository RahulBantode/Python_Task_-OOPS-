''' Statement : write a program which accept number from user and check whether that number is positive or 
				negative or zero 
'''

def CheckNumber(value):
	if value > 0 :
		return 1
	elif value < 0 :
		return -1
	else:
		return 0

def main():
	no = int(input("Enter the number : "))

	ret_value = CheckNumber(no)

	if ret_value == 1:
		print("Number {} is positive".format(no))
	elif ret_value == -1:
		print("Number {} is negative".format(no))
	else:
		print("Number {} is zero".format(no))

if __name__ == '__main__':
	main()
