''' problem statement :-
write a program which contains filter(),map(),reduce() function 
step 1 = filter should filter out all the prime numbers
step 2 = Map function will multiply each number by 2
step 3 = reduce function will find the maximum amongst all '''

from functools import *

def CheckPrime(no):
	i = 2
	
	sq_root = no/2
	flag = True
	while i <= sq_root:
		if no % i == 0:
			flag=False
		i = i+1

	return flag 

def Maximum(value1,value2):
	if value1 < value2:
		return value2
	else:
		return value1

def main():
	List = []
	size = int(input("Enter the size of list : "))

	for i in range(size): 
		List.append(int(input("Enter the element : ")))

	print("Accepted list : ",List)

	PrimeList = list(filter(CheckPrime,List))
	print("Prime Nos : ",PrimeList)

	MultiplyList = list(map(lambda no : no*2,PrimeList))
	print("Multiply by 2 list : ",MultiplyList)

	Max = reduce(Maximum,MultiplyList)
	print("Maximum no. in list : ",Max)

if __name__ == '__main__':
	main()
