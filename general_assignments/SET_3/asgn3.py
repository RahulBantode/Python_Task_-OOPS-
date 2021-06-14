#SET=3 Write a function to check if sub string is present in given string 

def sub_string_checker(string):
	
	split_string=string.split()
	length=len(split_string)

	return length



string=input("Enter the string = ")

count=sub_string_checker(string)

if count == 1:
	print("The string ",string,"not have substring")
else:
	print("The string ",string,"have ",count-1,"no. of substrings")



