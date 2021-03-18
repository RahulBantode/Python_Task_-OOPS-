'''Demonstration static method,class method,instance method 
 '''
class Student:
	School = "Lokmanya Vidyalay" #class variable

	def __init__(self,no1,no2,no3):  #init method which works like constructor
		self.m1 = no1     #instance variable
		self.m2 = no2
		self.m3 = no3

	def InstanceTotal(self):  #instance method
		print("Inside instance method")
		return self.m1 + self.m2 + self.m3


	@classmethod 				#it known as decorator which conveys the compiler that it is class method 
	def ClassDisplaySchool(cls):   #class method    cls is for showing that it is a class method
		print("School Name is : ",cls.School)

	@staticmethod               #its decoration which converys the compiler that it is static method
	def StaticInfo():
		print("This class contains the information of school")


def main():
	Student.ClassDisplaySchool() #calling class method

	obj_1 = Student(75,65,97)    #creating the object
	obj_2 = Student(88,99,65)

	print("Total marks of Student obj_1 : ",obj_1.InstanceTotal())
	print("Total marks of Student obj_2 : ",obj_2.InstanceTotal())

	Student.StaticInfo()		#calling the static method

if __name__ == '__main__':
	main()