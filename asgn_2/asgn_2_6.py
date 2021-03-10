''' statement :- display following pattern for user entered number of times
				 * * * * *
				 * * * *
				 * * *
				 * *
				 *
				 '''

def PrintStar(no):
	row = no
	while row >= 1:
		col = 1
		while col<=row:
			print("*\t",end=" ")
			col = col+1

		print()
		row = row-1

def main():
	value = int(input("How many times you want to entered < * > : "))
	PrintStar(value)

if __name__ == '__main__':
	main()