'''Problem Statement :

	wap which accept file name from user and create new file named as demo.txt
	and copy all the contents from existing file to new file.Accept the file name through 
	command line arguments.

'''

from sys import *

def main():

	if len(argv) < 2 :
		print("Inappropriate command line arguments (only 2 is required please check it)")
		return

	try:
		fobj1 = open(argv[1],'r')
		fobj2 = open('Demo.txt','w')

	except Exception as ex:
		print("Exception : ",ex)

	else:
		msg = fobj1.read()
		fobj2.write(msg)
		fobj1.close()
		fobj2.close()
		print("File operation successfully done")

if __name__ == '__main__':
	main()
