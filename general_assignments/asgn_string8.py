'''A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program that asks the user for a string and returns an estimate of how
many words are in the string.'''

string=input('Enter the String = ')

wrd=1
sp=0
ch=0
for ch in range(len(string)):
	if string[ch]=='\n':
		wrd=wrd+1
	
	elif string[ch]==' ':
		sp=sp+1
		wrd=wrd+1
	else:
		ch=ch+1

print("The no of spaces in string are =",sp)
print("The no of words in string are= ",wrd)
print("The no of characters are= ",ch)