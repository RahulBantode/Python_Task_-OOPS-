'''problem statement :- display below pattern using recursion 
input = 5
output= 1 2 3 4 5
'''
i=1
def PrintPattern(no):
	global i
	if i <= no:
		print(i," ",end=" ")
		i = i + 1
		PrintPattern(no)

def main():
	value = int(input("Enter the number : "))
	PrintPattern(value)

if __name__ == '__main__':
	main()