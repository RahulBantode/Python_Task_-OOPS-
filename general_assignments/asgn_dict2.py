'''For this problem, use the dictionary from the beginning of this chapter whose keys are month
names and whose values are the number of days in the corresponding months.
(a) Ask the user to enter a month name and use the dictionary to tell them how many days
are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
(d) Print out the (key-value) pairs sorted by the number of days in each month'''

days={'jan':31,'feb':28,'march':31,'april':30,
	  'may':31,'june':30,'jully':31,'aug':30,
	  'sep':31,'oct':30,'nov':31,'dec':30}

month=input("Enter the name of month =")
m=month.lower()

#part a
for d in days:
	if m==d:
		print("The no. of days =",days[d],"\n")



#part b
print("The All the months in alphabetical order = \n")

months=list(days)
months.sort()
for m in months:
	print("  ",m,end="\n")


#part c
print("\n The months which has 31 days in it = \n")
for d in days:
	if days[d]==31:
		print("\t",d)


#part d
print("\n The key value sorted according to no. of days in months =\n")

months_days=list(days.items())
months_days=[( i[1],i[0] ) for i in months_days]
months_days.sort()
for i in months_days:
	print("\t  ",i,end="\n")


#Its my define part
print("\n The key value sorted according to months (alphabetical) =\n")

months_days=list(days.items())
months_days.sort()
for i in months_days:
	print(" ",i,end="\n")
