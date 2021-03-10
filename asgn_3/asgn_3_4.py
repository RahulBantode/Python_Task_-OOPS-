'''problem statement :-
Write a Program which accept N numbers from user and store it into List.
Accept one number from user and return frequency of that number (return number of occurence count )
input = 2 44 2 5 2
search = 2
output = 3
'''

		
def FrequencyNumber(List,value):
	counter = 0
	for i in range(len(List)):
		if value == List[i]:
			counter = counter + 1

	return counter
			
def main():
	arr = []
	size = int(input("Enter the size of list : "))

	for i in range(size):
		arr.append(int(input("Enter the element : ")))

	print("Accepted Data is    : ",arr)

	value_to_search = int(input("Enter the number to find frequency : "))
	
	fre_number = FrequencyNumber(arr,value_to_search)
	print("Frequency of Number {} : {}".format(value_to_search,fre_number))

if __name__ == '__main__':
	main()