'''Write a program that asks the user to enter a string, then prints out each letter of the string
doubled and on a separate line. For instance, if the user entered HEY, the output would be
HH
EE
YY'''


string=input('Enter the string = ')

for ch in range(len(string)):
	print(string[ch]*2,end="\n")

'''op-
Enter the String= rahul
rr
aa
hh
uu
ll