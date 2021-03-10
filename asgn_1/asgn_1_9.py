''' statement :- write a program which accept name from user and display length of its name
'''

def main():
	accept_str = input("Enter the string : ")
	print("Length of <{}> string : {}".format(accept_str,len(accept_str)))

if __name__ == '__main__':
	main()
