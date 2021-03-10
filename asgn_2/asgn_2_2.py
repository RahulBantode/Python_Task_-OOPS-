''' Statement : Write a program which accept one number and display below pattern
				* * * * 
				* * * *
				* * * *
				* * * *
				'''

def PrintStar(value):
	row =1
	while row <= value:
		col = 1
		while col <= value:
			print("*\t",end=" ")
			col = col+1
		print()
		row = row+1
def main():
	number = int(input("Enter the number : "))
	print("Pattern of {} : ".format(number))

	PrintStar(number)

if __name__ == '__main__':
	main()