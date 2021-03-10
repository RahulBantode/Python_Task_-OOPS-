''' Statement : wap which accepts one number and display following pattern
1 2 3 4 5
2 3 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

def PrintNumbersPattern(no):
	row = 1
	while row <= no:
		col = 1
		while col <= no:
			print(col," ",end=" ")
			col = col+1

		print()
		row = row+1

def main():
	value = int(input("Enter one number : "))
	PrintNumbersPattern(value)

if __name__ == '__main__':
	main()