'''Problem Statement :- Write a recursive program which accept number from user and return
summation of its digits. 
input = 123
output= 6
'''
sum = 0
def SummationDigits(num):
	global sum

	if num != 0 :
		remainder = num % 10
		sum = sum + remainder
		new_num = num // 10
		SummationDigits(new_num)

	return sum
	
def main():
	number = int(input("Enter the number : "))
	sum_digits = SummationDigits(number);

	print("Sum of number of digits {} : {}".format(number,sum_digits))

if __name__ == '__main__':
	main()