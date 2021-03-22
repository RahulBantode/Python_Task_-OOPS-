'''Problem Statement :
   Write a program which accept two file names from user and compare contents of both files.
   If both the file contains same contenets then display success otherwise display failure.
   Accept both the names of through command line

 '''

#to compare the contents of the file python gives module name filecmp which having cmp method

from filecmp import *
from sys import *

def main():

	if len(argv) < 3 :
		print("Inappropriate command line arguments")

	fobj_1 = open(argv[1],'r')
	fobj_2 = open(argv[2],'r')

	#fobj1.fileno() :- it gives the file descriptor - so from fd we can conclude that file is opened
	                 # if it return -1 then file is unable to open

	if fobj_1.fileno() != -1 and fobj_2.fileno() != -1:
		print("Both files successfully opened")
		if cmp(argv[1],argv[2]):
			print("Both files have equal contents")
		else:
			print("Bothe file have not equal contents")

	else:
		print("File unable to open")

	fobj_1.close()
	fobj_2.close()


if __name__ == '__main__':
	main()