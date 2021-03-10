'''Write a program that asks the user to enter some text and then counts how many articles are
in the text. Articles are the words 'a', 'an', and 'the'.'''

text=input('Enter the some text =\n')
text2=text.split()

cnt=0

for i in range(len(text2)):
	if text2[i]=='a' or text2[i]=='A': 		
		cnt=cnt+1

	elif text2[i]=='the' or text2[i]=='The' or text2[i]=='THE':
		cnt=cnt+1

	elif text2[i]=='an' or text2[i]=='An' or text2[i]=='AN':
		cnt=cnt+1


print("The no. of articles in this text = ",cnt)