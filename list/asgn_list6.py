'''
5. Ask the user to enter a list of strings. Create a new list that consists of those strings with their
first characters removed.'''

list_string=eval(input('Enter the list of string ='))

for i in range(len(list_string)):
	for j in range(len(list_string[i])):
		if list_string[j]==0:
			new_string= del list_string[j]

		else:
			new_string=list_string[j]

print('New String = ',new_string)