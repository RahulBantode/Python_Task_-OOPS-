number=eval(input("Enter the binary number = "))

decimal=0
decimal_point=24
for i in range(number):
	decimal=decimal+decimal_point * i
	decimal_point=decimal_point-1

print("The binary number = ",number)
print("After convert to decimal")
print("Decimal number = ",decimal)