''' Using the card dictionary from earlier in this chapter, create a simple card game that deals
two players three cards each. The player with the highest card wins. If there is a tie, then
compare the second highest card and, if necessary, the third highest. If all three cards have
the same value, then the game is a draw. '''

#this is import for the shuffle function...
from random import shuffle


deck=[{'value':i , 'suit':c}
	  for c in ['spades','club','hearts','diamonds']
	  for i in range(2,15)]

shuffle(deck)

player1=input("Enter the Name = ")
player2=input("Enter the Name = ")

#this is for selecting random items from list with how much selcection
from random import sample

player_1=sample(deck,3)
player_2=sample(deck,3)

pl1=0 #counters
pl2=0 #counters

print(player_1,end="\n")
print(player_2,end="\n")

for i in range(len(player_1)):
	for j in range(len(player_2)):
		if player_1[{deck}] < player_2[{deck}]:
			pl2=pl2+1

		elif player_1[{deck}] > player_2[{deck}]:
			pl1=pl1+1

		elif player_1[{deck}] == player_2[{deck}]:
			pl1=pl1+1
			pl2=pl1+2


if pl1<pl2:
	print("The winner player = ",player1)
else:
	print("The winner player = ",player2)