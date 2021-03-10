''' Write a program that uses a dictionary that contains ten user names and passwords. The
program should ask the user to enter their username and password. If the username is not in
the dictionary, the program should indicate that the person is not a valid user of the system. If
the username is in the dictionary, but the user does not enter the right password, the program
should say that the password is invalid. If the password is correct, then the program should
tell the user that they are now logged in to the system.  '''


account={'rahul':999,'nitin':123,'kunal':456,
		 'manish':567,'sharma':290,'prashant':789,
		 'bhushan':213,'kalpesh':435,'akshay':721,
		 'nikhil':169}

username=input("Enter the username = ")
password=int(input("Enter the password = "))

if username not in account:
	print("\tThe invalid user, which are not user of system")

else:
	for ac in account:
		if account.get(ac)==password:
			print("Your username is ",ac,"\nyou are logged in to system")
			continue		
		else:
			print("\n \tPlease enter valid password")
			