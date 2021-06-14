'''Write a program that asks the user to enter a string s and then converts s to lowercase, removes
all the periods and commas from s, and prints the resulting string.'''

string=input('Enter the String = ')

print(string.lower(),end="\n")


for ch in range(len(string)):
	if string[ch]!=',':
		print(string[ch],end="")
	

