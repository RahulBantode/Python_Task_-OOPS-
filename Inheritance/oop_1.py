
class Rahul:
	value_1 = 1010   #class variable/static etc

	def __init__(self,no1,no2):  #its a constructor
		print("Inside the __init__ method")
		self.i = no1   #instances variable
		self.j = no2   #instances variable

	def __del__(self):	#its like destructor
		print("Inside the __del__ method")


	def Fun(self):		#instance method
		print("Inside the Fun method")
		print("Value of J : ",self.j)

	def Gun():
		print("Inside the class method Gun")

	Gun()

	def Mon():
		print("Inside the class method MOn")

	Mon()
	
def main():
	obj_1 = Rahul(11,33)
	obj_2 = Rahul(22,99)

	print("Value of i from obj_1 : ",obj_1.i) #accessing instance members
	print("Value of i from obj_2 : ",obj_2.i) 

	print("Value of class member : ",Rahul.value_1)

	obj_1.Fun()
	obj_2.Fun()

	del obj_1
	del obj_2   #by using this we deallocate the resouuce forcefully / immediate deallocation take place

if __name__ == '__main__':
	main()
