''' statement :- write a program which display  "jay shree mahakal" string 5 times on screen'''

def main():
	#here we explicitly pass starting and ending point to the range function
	#last point is excluded so we want 5 times printing so we pass end point as 6
	for i in range(1,6):
		print("{} . Jay Shree Mahakal".format(i))

if __name__ == '__main__':
	main()