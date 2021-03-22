'''Problem statement :-

write a program which aceepts file name from user and check whether that file
exists in current directory or not.
'''

from os import *

def main():
	fname = input("Enter the file name : ")
	
	if path.exists(fname):
		print("The file is exist in current directory")
	else:
		print("The file is not exist in current directory")	
		

if __name__ == '__main__':
	main()