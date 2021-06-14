'''13.	Write A Python Program to generate the Fibonacci sequence, Factorial of the number
       using user defined function.'''



def fact(fact_num):
	result=1
	i=1
	while i <= fact_num :
		result=result * i

		i=i+1

	return result	

given_number=int(input("Enter the given number to find factorial = "))

factorial_number=fact(given_number)

print("The factorial of number =",given_number,"! =",factorial_number)
