'''problem statement :- display below pattern using recursion 
input = 5
output= 5  4  3  2  1
'''

def PrintPattern(no):

	if no != 0:
		print(no," ",end=" ")
		no = no - 1
		PrintPattern(no)

def main():
	value = int(input("Enter the number : "))
	PrintPattern(value)

if __name__ == '__main__':
	main()