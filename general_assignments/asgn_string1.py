#Demonstrate the program which implements string methods--

string1='Rahul bantode from IICMR nigdi'
string2='K0unal Chinchole from MCA,codewarriors'

string3=string1+string2 #here concatenation of string taken place

print(string1.lower())#print every letter in string in lower case

print(string2.upper())#print every letter in string in upper case

print(string3.replace('a','#'))#returns string with every occurence of first argument replace with second args

print(len(string1))

print(string2.count('a'))#count the given arg. which appear how much time in string

print(string1.index('a'))#here returns the index of first occurence of a

print(string1.index('a',3,9))#here returns the index of a from start index 3 to 9

print(string1[0].isalpha())#it returns true if all the character is letter otherwise returns false

print(string2[1].isalnum())#it returns true if all the character is digits otherwise returns false

#many of the string methods if you want to see then type dir(str) on command prompt you will appear those methods