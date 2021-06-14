'''prog. to demonstrate the queue opera. on list'''

from collections import deque

queue=['Rahul',9,'Nitin',6,'kunal',55,'nikhil']

print("The length of queue is =",len(queue))
print("The list is =",queue)

print()

item=input("Enter the item =")
queue.append(item)
print("The list is =",queue)

item=input("Enter the item =")
queue.append(item)
print("The list is =",queue)

popitem=queue.popleft() 
print("Removed element =",popitem)

popitem=queue.popleft() 
print("Removed element =",popitem)

popitem=queue.popleft() 
print("Removed element =",popitem)

print("The list is =",queue)

'''dont recognize the problem
appendleft(),popleft() are the function related to
list. but interpreter gives and error like
list object has no popleft and appendleft so 
first search on it'''