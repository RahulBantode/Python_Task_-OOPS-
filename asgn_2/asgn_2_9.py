''' statement : wap which accept number from user and return how many number of digits in that number
	ip = 12345 op=5
'''

def CountDigits(number):
	counter = 0
	new_number = 0

	while number != 0:
		new_number = number // 10
		counter = counter + 1
		number = new_number

	return counter

def main():
	no = int(input("Enter the number : "))

	length_number = CountDigits(no)

	print("The length of {} : {}".format(no,length_number))

if __name__ == '__main__':
	main()