'''SET 3= Write A Python program to Python Program for Sum of squares of first n natural numbers'''

def squares(n):
	
	return n**2


n=int(input("Enter the range of natural nos ="))

i=1
sum=0

while i <= n:

	sum=sum+squares(i)
	i=i+1

print("The sum of ",n,"^th Natural nos are =",sum)

