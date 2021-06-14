#SET 2=Write A Python Program to Find the Largest Among Three Numbers

print("Enter the three numbers(while enter number after entering first then hit enter key then second")

no1=int(input())
no2=int(input())
no3=int(input())

if no1 > no2 and no1 > no3:
	print("The number",no1,"is largest")

elif no2 > no1 and no2 > no3:
	print("The number",no2,"is largest")

elif no3 > no1 and no3 > no2:
	print("The number",no3,"is largest")