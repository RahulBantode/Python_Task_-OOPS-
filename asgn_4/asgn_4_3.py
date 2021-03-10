'''Problem Statement :-
write a program which contains filter(),map(),reduce() in it. Python application which
contains one list of numbers. List contains the number which are accepted from user.
Filter should filter out all the such numbers which greater than or equal to 70 and less than or equeal to 90.
Map function will increase each number by 10.
Reduce will return the product of all numbers. '''

from functools import *

def Filteration(no):
	if (no >= 70) and (no <= 90):
		return True
	else:
		return False

def Increment(no):
	return no + 10


def main():
	List = []
	size = int(input("Enter the size of list : "))

	for i in range(size) : List.append(int(input("Enter the element : ")))

	print("Accepted list : ",List)

	FilteredList = list(filter(Filteration,List))
	print("After Filteration : ",FilteredList)

	MappedList = list(map(Increment,FilteredList))
	print("After Mapped : ",MappedList)

	ReduceProduct = reduce(lambda no1,no2 : no1*no2,MappedList)
	print("Product of all : ",ReduceProduct)

if __name__ == '__main__':
	main()