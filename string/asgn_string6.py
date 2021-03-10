'''(a) The seventh character of the string if the string is long enough and a message otherwise
The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e'''


string=input('Enter the String...')

for i in range(len(string)):
	if i==7:
		print("The string is too long...")
	

print("The all letters of string in capitals=",string.upper())

print("Replace string with every a with e=",string.replace('a','e'))

print("Removed the first and last characters of string=",string[1:-2])
'''strip() method removes the traling and ending character 
from the string this has one optional argument where
we can give the set of string from where to remove
 
 but there is proble in it that they return exact 
 copy of the string

 so we use slice method 

'''





