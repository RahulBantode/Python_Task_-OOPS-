'''(a)The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards'''

string=input('Enter the string...')

print('First character of string=',string[0])

print('First three character of string=',string[0:2])

print('last three character of string=',string[-1],string[-2],string[-3])

i=len(string)
#there is two option or many more for reverse
# we use slicing

print("The reveresed the string =",string[i::-1])
print("The reveresed the string =",string[::-1])


	
	