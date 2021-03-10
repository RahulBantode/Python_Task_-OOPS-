'''Problem statment :-
WAP which accept N numbers from users and store it into list.
Return addition of all elements from that list. '''

Addition = lambda value1,value2 : value1+value2

def CalculateAdd(List):
	add = 0
	for i in range(len(List)):
		add = Addition(add,List[i])

	return add

def main():
	arr = []
	size = int(input("Enter the size of list : "))

	for i in range(size):
		arr.append(int(input("Enter the element : ")))

	print("Accepted Data    : ",arr)
	print("Addition of list : ",CalculateAdd(arr))

if __name__ == '__main__':
	main()