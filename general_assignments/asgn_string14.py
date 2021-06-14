

no=int(input('Enter how much email you want to insert ='))

std=0
prof=0
i=0
while(i<no):
	email=input('Enter the emails address = ')
	i=i+1

while(i<no):
	if email[i].stratswith('@student'):
		std=std+1
		i=i+1

	if email[i].stratswith('@professor'):
		prof=prof+1
		i=i+1

print('The students address  = ',std)
print('The professor address = ',prof)

#something missing