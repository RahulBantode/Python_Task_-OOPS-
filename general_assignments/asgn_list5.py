'''Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
entries in the list that are greater than 10 with 10.'''

list=eval(input('Enter the List containing no.(1to12)\n'))

print("The list no between 1 to 12 are...")
for i in range(len(list)):
	if list[i]>=1 and list[i]<=12:
		print(list[i],end=',')
	else:
		print('\n\nList not containing no. between 1 to 12=',list[i])

for i in range(len(list)):
	if list[i]>10:
		list[i]=10

print("\nThe list after replacement effect..=",list)

