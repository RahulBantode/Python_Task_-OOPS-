'''problem statment :
Write a Program which accept N numbers from user and store it into List.
Return addition of all prime numbers from that list. 

main python file asgn_3_5.py = file accept n numbers from user and pass to CheckPrime() function
MarvellousNum.py = CheckPrime() function which are user defined module
asgn_3_5.py - ListPrime function

'''
from MarvellousNum import *
from functools import *

def main():
	arr = []
	size = int(input("Enter the size of list : "))

	for i in range(size):
		arr.append(int(input("Enter the element : ")))

	print("Accepted Data is    : ",arr)

	PrimeList = list(filter(CheckPrime,arr))
	print("Prime numbers list = ",PrimeList)

	Addition = reduce(lambda no1,no2 : no1+no2,PrimeList)
	print("Addition of numbers : ",Addition)

if __name__ == '__main__':
	main()
	