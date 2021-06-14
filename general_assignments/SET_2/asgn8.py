#SET=Program to check Armstrong numbers in a certain interval(means in between yoou have to check)

lower=int(input("Enter the Lower range ="))
upper=int(input("Enter the Upper range ="))

#num=lower

for num in range(lower,upper+1):
	sum=0

	copyno=num

	while num != 0:
		rem= num % 10
		sum= sum+rem*rem*rem
		num= num//10

	if sum == copyno:
		print('\n',copyno,"= Armstrong no")
	

