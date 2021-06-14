#simple quiz game

question=['What is the capital of france ?\n','Which state has no neibour ?\n']

answer=['paris','maine']
num=0
for i in range(len(question)):
	guess=input(question[i])
	if guess.lower()==answer[i].lower():
		print('Correct')
		num=num+1
	else:
		print('Sorry,Incorrect... The correct answer is',answer[i])

print('\nYour total score is ',num)

'''The benefits of this are that to change a 
question, add a question, or change the order,
only the questions and answers lists need to be 
changed. Also, if you want to make a change to the
program, like not telling the user the correct 
answer, then all you have to do is modify a 
single line, instead of twenty copies of that 
line spread throughout the program.'''