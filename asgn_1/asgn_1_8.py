''' statement : write a program which accept number from user and print that number of * on screen'''

def PrintStar(value):
	i=1
	while i <= value:
		print("*\t",end=" ")
		i = i+1

def main():
	no = int(input("How many times you want print \"*\" on screen : "))

	PrintStar(no)

if __name__ == '__main__':
	main()
