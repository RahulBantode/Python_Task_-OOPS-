'''statement : Write a program which display first 10 even numbers on screen'''

def PrintEven():
	i=1
	cnt=0

	while cnt != 10:
		if i % 2 == 0:
			print(i,"\t",end=" ")
			cnt = cnt+1

		i = i+1
		 

def main():
	print("First 10 even numbers are as follows : ")
	PrintEven()

if __name__ == '__main__':
	main()