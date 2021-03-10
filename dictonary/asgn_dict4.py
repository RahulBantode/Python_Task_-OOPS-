'''  Repeatedly ask the user to enter a team name and the how many games the team won and
how many they lost. Store this information in a dictionary where the keys are the team names
and the values are lists of the form [wins, losses].
(a) Using the dictionary created above, allow the user to enter a team name and print out
the team’s winning percentage.
(b) Using the dictionary, create a list whose entries are the number of wins of each team.
(c) Using the dictionary, create a list of all those teams that have winning records. '''

scores={}
teams=int(input("How many teams are there = "))

for i in range(teams):

	team_name=input("Enter the team name =")
	wons=int(input("How much won  = "))
	lost=int(input("How much loss = "))

	scores[team_name]=[wons,lost]

print("\nThe data of the dictionary =")
for d in scores.items():
	print(d)

#part a

team_nm=input("\nEnter the team name to calculate the winning percentage =")

if team_nm in scores:
	print("The winning percentage of ",team_nm," = "
	,(scores[team_nm][0]/sum(scores[team_nm]))*100)
else:
	print("There is no such team was participated")


#part b
print("\n The list of the won of all teams = ")

w_team=[i[0] for i in scores.values()]
print("\t",w_team,"\n\n")
'''yat to scores.values tyat value tyala bhetel
then i[0] mhnje 0 pos. la won je aahe te aahe
so te to kadhun deil'''

'''
#part c
#error
w_rec=[[]for i in scores]

if socres[i][0] > 0:
	w_rec.append(i)

print(w_rec)'''