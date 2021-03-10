'''problem statment :-
write a program which accept n numbers from user and store it into list. return minimum number from list '''


def Minimum(value1,value2):
	if value1 < value2:
		return value1
	else:
		return value2

def FindMinimum(List):
	min = List[1]
	for i in range(len(List)):
		min = Minimum(min,List[i])

	return min

def main():
	arr = []
	size = int(input("Enter the size of list : "))

	for i in range(size):
		arr.append(int(input("Enter the element : ")))

	print("Accepted Data is    : ",arr)
	print("Minimum between all : ",FindMinimum(arr))

if __name__ == '__main__':
	main()

