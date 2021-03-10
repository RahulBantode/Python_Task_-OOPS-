'''Write a program that asks the user to enter a string. The program should create a new string
called new_string from the user’s string such that the second character is changed to an
asterisk and three exclamation points are attached to the end of the string. Finally, print
new_string. Typical output is shown below:
Enter your string: Qbert
Q*ert!!!'''

string=input('Enter the String = ')

new_str=string

for ch in range(len(string)):
	if ch==1:
		new_str=string.replace(string[ch],'*')

print(new_str+'!'+'!'+'!')

'''
mhnje aapn eka string vr operation kraychi 
aani tila dusrya string mdhe assign kraychi teva
aaplya effect disun yeto tyashivay yet nahi

same string mdhech ts kel tr ti only copy return 
krun dete'''