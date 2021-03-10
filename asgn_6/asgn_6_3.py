'''Problem Statment :- 3
Write a program which contains one class named as Arithmetic .
Arithmetic class contains three instance varibles as value_1,value_2.
Inside the init method initiallize all the variables to 0.

There are following instance methods inside the class are:
Accept() , Addition(), Substraction(), Multiplication(), Division(),Display()
'''
class Arithmetic:

	def __init__(self):
		self.value_1 = 0
		self.value_2 = 0
	
	def Accept(self):
		self.value_1 = int(input("Enter the 1st number : "))
		self.value_2 = int(input("Enter the 2nd number : "))
		print()

	def Addition(self):
		return self.value_1 + self.value_2

	def Substraction(self):
		return self.value_1 - self.value_2

	def Multiplication(self):
		return self.value_1 * self.value_2

	def Division(self):
		return self.value_1 / self.value_2

	def DisplayResult(self):
		print("Addition       : ",self.Addition())
		print("Substraction   : ",self.Substraction())
		print("Multiplication : ",self.Multiplication())
		print("Division       : ",self.Division())

def main():

	obj_1 = Arithmetic()
	obj_1.Accept()
	obj_1.DisplayResult()
	print("--------------------------")

	obj_2 = Arithmetic()
	obj_2.Accept()
	obj_2.DisplayResult()
	print("--------------------------")

	obj_3 = Arithmetic()
	obj_3.Accept()
	obj_3.DisplayResult()
	print("--------------------------")

if __name__ == '__main__':
	main()