'''12. Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS.'''

string=input('Enter the string = ')


i=1

for i in range(len(string)):
	if i % 2 == 0:
		print(string[i].lower(),end="")

	else:
		print(string[i].upper(),end="")

