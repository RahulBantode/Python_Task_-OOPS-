#4.	Python program to split a string and join it using different delimiter 


accept_string=input("Enter the string = ")

split_string=accept_string.split()

accept_delimeter=input("Enter the delimeter by using it you want to join the string =")
print(split_string)
for i in split_string:
	if i == " ":
		print(accept_delimeter,end=" ")
	else:
		print(i,end=" ")

