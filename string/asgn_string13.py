#check whether the given string is pallindrome or not

string=input('Enter the string=')

#logic to reversed the string using slicing
# string lenght=9 tithun -1 prynt mhnje ult yaych
reversed_string=string[len(string)::-1]

if(string==reversed_string):
	print("The String is pallindrome")

else:
	print("The string is not pallindrome")