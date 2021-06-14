'''Write a program that asks the user to enter two strings of the same length. The program
should then check to see if the strings are of the same length. If they are not, the program
should print an appropriate message and exit. If they are of the same length, the program
should alternate the characters of the two strings. For example, if the user enters abcde and
ABCDE the program should print out AaBbCcDdEe.'''

string1=input('Enter the string 1st = ')
string2=input('Enter the string 2nd = ')

length1=len(string1)
length2=len(string2)


if length1==length2:
	ch=0
	while(range(len(string1))):
		print(string1[ch],end='')
		ch=ch+1
		break

	ch=0
	while(range(len(string2))):
		print(string2[ch],end='')
		ch=ch+1
		continue
else:
	print('The string length doesn\'t match')

#Not completed this