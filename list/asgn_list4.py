'''Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]'''

List=[8,9,10]

List.insert(1,17)
print("The list after inserting 17..",List,'\n')


List.append(4)
List.append(5)
List.append(6)
print("The list after appending 4,5,6 =",List,'\n')

List.pop(1)
print("The list after remove first entry =",List,'\n')

List.sort()
print("The sorted List=",List,'\n')

List2=List
List3=List+List2
print("The double the list=",List3,'\n')

List3.insert(3,25)

print("The list after inserting 25..",List3,'\n')

