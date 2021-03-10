'''statement : wap which accept from user and return addition of digits in that numbers
ip = 1234  op =10
'''

def AdditionDigits(number):
	sum_digit = 0

	while number != 0:
		adder = number % 10
		sum_digit = sum_digit + adder
		number = number // 10

	return sum_digit

def main():
	no = int(input("Enter one number : "))
	addition_digits = AdditionDigits(no)

	print("Addition of {} : {}".format(no,addition_digits))

if __name__ == '__main__':
	main()