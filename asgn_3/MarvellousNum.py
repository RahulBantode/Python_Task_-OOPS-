
def CheckPrime(no):
	i = 2
	
	sq_root = no/2
	flag = True
	while i <= sq_root:
		if no % i == 0:
			flag=False
		i = i+1

	return flag 
