'''Write a program that allows the user to enter five numbers (read as strings). Create a string
that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2,
5, 11, 33, and 55, then the string should be '2+5+11+33+55'.'''

no=input('Enter the five numbers string = ')

for i in range(len(no)):
	if no[i]==' ' or no[i]=='\n':
		print(new)
	else:
		new_string=no[i]


print('The string = ',new_string)