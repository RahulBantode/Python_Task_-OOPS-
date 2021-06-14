#set2 2.Write A Python Program to check if the Number is perfect Number.

number=int(input("Enter the Number ="))

copynumber=number #its for varifying sum is equal to number

rem=0
sum=0
i=1

'''aapn number-1 ka ghetl becz shevti i ha equal to 
actual num hoiel so to pn tyacha divisor mhnun count
kela jaiel karn jya no ne tya no la divide kel tr
rem 0 yete so tyane count chukel mhnun
'''
while i<=(number-1):
	rem=number % i

	if rem==0 :
		sum=sum+i

	i=i+1

if sum==copynumber:
	print("The number ",copynumber,"is perfect number")

else:
	print("The number ",copynumber,"is not perfect number")


'''DEF oof perfect no=
The sum of all positive divisor of the number is equal
to number called as perfect number
ex= no=6
divisor =1,2,3
the sum=6 so 6 is equal to 6 so it is perfect no.