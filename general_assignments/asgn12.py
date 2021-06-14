'''program using list as a stack in python & perform all the
operation of stack'''

list=['rahul',2,'nitin',9,'kunal',25,2]
print("The length of list =",len(list))

x=input("Enter the elment in stack of list =")
list.append(x)

y=input("Enter the element in stack of list=")
list.append(y) #method add element at last

print("The list = ",list)

z=list.pop()#this method remove element from last
print("The popped element =",z)

a=list.pop()
print("The popped element =",a)

b=list.pop()
print("The popped element =",b)

print("The list = ",list)

