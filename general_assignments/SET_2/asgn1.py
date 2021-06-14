#set2 1.Write A Python Program to Swap Two Variables.

var1=int(input("Enter the no ="))
var2=int(input("Enter the no ="))

temp=0 #this can be used for temporary store the value

print("\nThe value before swapping")
print("var1 =",var1, " var2 =",var2)

temp=var1
var1=var2
var2=temp

print("\nThe value After swapping")
print("var1 =",var1, " var2 =",var2)