'''Problem Statement :- write a program which contains lambda function which accepts one paremeter and return
power of two
input 4 output 16
input 6 outpue 36

'''

Power = lambda value :  value * value

def main():
	number = int(input("Enter the number : "))
	power_no = Power(number)
	#power_no = lambda number :  number * number #it gives an error lambda declare in local main
	print("The Power of base {} to the exponent 2 is : {}".format(number,power_no))

if __name__ == '__main__':
 	main() 