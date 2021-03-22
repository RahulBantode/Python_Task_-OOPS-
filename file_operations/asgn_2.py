'''Problem Statement :
	write a program which accept the filename from user and open that file and display the
	contents of that file on screen
'''

def main():
	fname = input("Enter the Filename : ")
	try:
		fobj = open(fname,'r')
		print(fobj.read())

	except FileNotFoundError as fex:
		print("Exception : ",fex)
	
	else:
		print("File operation successful")
		fobj.close()

if __name__ == '__main__':
	main()