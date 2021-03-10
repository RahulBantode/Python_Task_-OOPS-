'''problem statement:
write a program which contains filter(), map(), reduce() function
Python application which contains one list of numbers.List contains the numbers which are accepted from user
filter should calculate all such number which are even
map function will calculate its square
reduce function will return the addition of all numbers '''

from functools import *

def main():
	List = []
	size = int(input("Enter the size of list : "))

	for i in range(size) : List.append(int(input("Enter the element : ")))

	print("Accepted list : ",List)

	EvenList = list(filter(lambda no : no % 2 == 0,List))
	print("Even nos list : ",EvenList)

	SquareList = list(map(lambda no : no * no , EvenList))
	print("Square of nos list : ",SquareList)

	Addition = reduce(lambda no1,no2 : no1+no2,SquareList)
	print("Addition of nos : ",Addition)

if __name__ == '__main__':
	main()