'''statement :- wap which accept one number for user and check whether number is prime or not'''

def CheckNumberPrime(no):
	i = 2
	
	sq_root = no/2
	flag = 0
	while i <= sq_root:
		if no % i == 0:
			flag=1
		i = i+1

	return flag 

def main():
	number = int(input("Enter the Number : "))
	ans = CheckNumberPrime(number)

	if ans == 0:
		print("Number {} is prime number".format(number))
	else: 
		print("Number {} is not prime number".format(number))

if __name__ == '__main__':
	main()