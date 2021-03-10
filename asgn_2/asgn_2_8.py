''' statement : accept one number from user and display below pattern.
1
1 2
1 2 3
1 2 3 4
1 3 3 4 5
'''

def PrintNumberPattern(no):
	row = 1
	while row <= no:
		col = 1
		while col <= row:
			print(col," ",end=" ")
			col = col + 1

		print()
		row = row + 1

def main():
	value = int(input("Enter one number : "))
	PrintNumberPattern(value)

if __name__ == '__main__':
	main()