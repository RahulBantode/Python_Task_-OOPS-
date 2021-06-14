'''People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has the same number of opening
and closing parentheses.'''

string=input("Enter the Formula=")

for ch in range(len(string)):
	if string[ch]!=')':
		print(string[ch],end="")

	elif string[ch]==')':
		print(string[ch],end="")

	else:
		print(string[ch],end="")


#incomplete logic