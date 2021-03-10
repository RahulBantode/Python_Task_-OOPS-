'''write a program to ask user to enter the word
and count the any vowel present their '''

word=input('Enter the Word=')
cnt=0
for i in range(len(word)):
	if (word[i]=='a' or word[i]=='e' or word[i]=='i' or
		word[i]=='o' or word[i]=='u' or word[i]=='A' or 
		word[i]=='E' or word[i]=='I' or word[i]=='O' or 
		word[i]=='U'):
			cnt=cnt+1



print("The vowels in this word =",cnt)


#here oprator is like or ... and by name directly
#|| && not usful here