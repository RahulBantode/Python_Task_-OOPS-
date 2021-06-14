#String with every letter replaced by space

string=input('Enter the string= ')
	
i=0
l=len(string)
while(string[i]!=l):
	string.replace(string[i]," ")
	i=i+1

print('-----The string blank now--------')
#it the uncomplete program