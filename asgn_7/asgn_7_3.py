'''Problem Statement :-
Wap which contains one class named as Arithmetic. Arithmetic class contains one instance variable as Value.
then implements the methods as CheckPrime() , CheckPerfect(), CheckFactors(), FactorSum(), Display()
'''

class Arithmetic:

	def __init__(self):
		self.value = 0;

	def Accept(self):
		self.value = int(input("Enter the value to check all the information : "))

	def CheckPrime(self):
		flag = False
		sq_rt = self.value//2

		for i in range(2,sq_rt+1):
			if self.value % i == 0:
				flag = True
				break

		return flag

	def CheckPerfect(self):

		sum = 0
		number = self.value
		for i in range(1,(self.value//2) +1):
			if self.value % i == 0:
				sum = sum + i

		if number == sum:
			return True
		else:
			return False

	def CheckFactors(self):

		fact = []
		for i in range(1,self.value):
			if self.value % i == 0:
				fact.append(i)

		return fact

	def FactorSum(self):
		sum = 0
		ans = self.CheckFactors()

		for i in range(len(ans)):
			sum = sum + ans[i]

		return sum

	def Display(self):
		print("---------------------------------------------------")
		ret_bool = self.CheckPrime()
		if ret_bool == False:
			print("Number is prime : {}".format(self.value))
		else:
			print("Number is not prime : {}".format(self.value))

		ret_bool = self.CheckPerfect()
		if ret_bool == True:
			print("Number is perfect : {}".format(self.value))
		else:
			print("Number is not perfect : {}".format(self.value))
		
		print("Factors of Numbers are : ",self.CheckFactors())
		print("Sum of factors are     : ",self.FactorSum())	
		print("---------------------------------------------------")

def main():

	obj_1 = Arithmetic()
	obj_1.Accept()
	obj_1.Display()

	obj_2 = Arithmetic()
	obj_2.Accept()
	obj_2.Display()

if __name__ == '__main__':
	main()