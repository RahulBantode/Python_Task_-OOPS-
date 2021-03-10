''' statement :- WAP  which accepts one number from user and return addition of its factors
	ip = 12 , factors of 12 is : 1,2,3,4,6, make addition of this numbers 1+2+3+4+6=16
'''

def FactorsAdditon(number):
	sum = 0
	i=1
	while i < number:
		if number % i == 0:
			sum = sum + i

		i = i+1

	return sum

def main():
	value = int(input("Enter the Number : "))
	addtion = FactorsAdditon(value)

	print("Addition of factors of {} : {}".format(value,addtion))

if __name__ == '__main__':
	main()