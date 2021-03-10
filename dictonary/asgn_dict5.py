''' Repeatedly ask the user to enter game scores in a format like team1 score1 - team2 score2. Store
this information in a dictionary where the keys are the team names and the values are lists of
the form [wins, losses]. '''

scores={}

while True:
	
	team_name=input("Enter the team name = ")
	score= int(input("Enter the Scores of team = "))
	won = int(input("Enter the no. of won  = "))
	loss= int(input("Enter the no. of loss = "))

	#sco[score]=[won,loss]

	scores[team_name]={score:[won,loss]}

	print("\nEnter the choice want to add (yes/no) ?")

	ch=input()
	choice=ch.lower()

	if choice!='yes':
		break


print("\n The Records of Teams = ")

for dic in scores.items():
	print("\t The team name = ",dic)

