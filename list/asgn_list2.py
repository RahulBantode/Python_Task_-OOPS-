'''Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the
result.

(g) Print how many integers in the list are less than 5.'''

List=[]
for i in range(43,58):
	List.append(i)

print("The List =",List,"\n")

print("The total no. of items in list =",len(List),"\n")

print("The Last item of the list =",List[-1],"\n")

List.reverse()
print("The list in reverse order =\n",List,"\n")

'''for i in range(len(List)):
	if i==5:
		print("Yes,List contains 5","\n")
	else:
		print("No,list not contains 5","\n")'''

print("The no. of 45 in list=",List.count(45),"\n")

first=List.pop(0)
last=List.pop(-1)

print("The first element removed from the list=",first,"\n")

print("The first element removed from the list=",last,"\n")
List.sort()
print("The sorted list after removing element=\n",List,"\n")


for i in range(len(List)):
	if List[i]<48:
		print("The no less than 48=",List[i])
