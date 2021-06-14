#set1 =10.	Write a Python Program to print ASCII Value of a character


#to find the ascii value of character 
#python gives built in function 'ord()'


character=input("Enter the character =")

print("The ASCII value of character",character,"=",ord(character))


#to find the character from  ascii value 
#python gives built in function 'chr()'
#this function strictly require int as argument
ASCII_value=int(input("Enter the ASCII_value ="))

print("The Character of ASCII value ",ASCII_value,"=",chr(ASCII_value))

