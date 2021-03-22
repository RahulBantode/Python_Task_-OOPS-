'''problem statement :-
   
   Accept the file name and one string from user and return the frequency of that string from file
   means to check whether the string is present in that file or not.

'''

def main():
	file_name = input("Enter the filename : ")
	string = input("Enter the string (to search in file) :")

	file_obj = open(file_name,'r')

	if file_obj.fileno() != -1:
		if string in file_obj.read():
			print("String is present in file ")
		else:
			print("String is not present in file")
	
	else:
		print("File unable to open")

	file_obj.close()

if __name__ == '__main__':
	main()