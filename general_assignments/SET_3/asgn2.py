#SET 3=Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term.

def addition(n):
	i=1
	sum=0
	while(i<=n):
		if sum==0:
			sum=sum+10+3
			print(sum ,end="+")
		else:
			sum=sum+10
			print(sum,end="+")
	
		i=i+1		


terms=int(input("Enter how many terms ="))
addition(terms)
	

#The code is remaining not solved completely