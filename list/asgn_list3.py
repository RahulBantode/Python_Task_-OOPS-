'''Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.'''

from random import randint
L = []
for i in range(20):
	L.append(randint(1,100))

print("The List=",L,'\n')

print("The average =",sum(L)/len(L),'\n')

L.sort()
print("List after sorted=",L)

print('The largest  =',L[-1],'\n')
print('The smallest =',L[0],'\n')

print('Second largest  =',L[-2],'\n')
print('Second smallest =',L[1],'\n')

for i in range(len(L)):
	if i%2==0:
		print("The even=",L[i])
	else:
		print("The odd=",L[i])
