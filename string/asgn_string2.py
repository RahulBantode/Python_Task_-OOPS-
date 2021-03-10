#Count the occurence of given character in string without using  built in function

string=input("Enter the string..\t")

ch=input("Enter the character to count..\t")

cnt=0
for i in range(len(string)):
	if string[i]==ch:
		cnt=cnt+1
		i=i+1
	elif i!=ch:
		i=i+1

print("The no of occurence of ",ch," is",cnt)	

'''for i in string:

if type only this then error is thrown on next line
so not use this type use range function which gives
index in int formats 

cnt=0
for i in string:
	if i==ch:
		cnt=cnt+1 this is also works 

because in for loop its operates on sequence of 
characters and iterable object so its directly
iterates not need to i=i+1 
'''

