'''problem statement :-
Write a Program which accept N numbers from user and store it into list.
Return Maximum number from the list
'''

def Maximum(value1,value2):
	if value1 < value2:
		return value2
	else:
		return value1

def FindMaximum(List):
	max = List[1]
	for i in range(len(List)):
		max = Maximum(max,List[i])

	return max

def main():
	arr = []
	size = int(input("Enter the size of list : "))

	for i in range(size):
		arr.append(int(input("Enter the element : ")))

	print("Accepted Data is    : ",arr)
	print("Maximum between all : ",FindMaximum(arr))

if __name__ == '__main__':
	main()

