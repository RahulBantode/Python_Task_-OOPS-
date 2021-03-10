'''Problem Statement :-2
WAP which contains one class named as Circle. Cicle class contains three instances variables as PI=which is
initialize to 3.14 . Inside init method initialise variables to 0,0,
There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display()

Accept method accept the value from user. 
CalculateArea() method will calculate area of circle and store it into instance variable Area.

CalculateCircumference() method will calculate the circumference of circle and store it into instance variable
Circumference

And Display() method will display value of all the instance variable as Radius,Area,Circumference

After designing the above class call all instances methods by creating multiple objects.
'''

class Circle:

	def __init__(self):
		self.PI = 3.14
		self.Radius = 0
		self.Area = 0
		self.Circumference = 0

	def Accept(self):
		self.Radius = int(input("Enter the Radius : "))

	def CalculateArea(self):
		self.Area = self.PI * (self.Radius ** 2)

	def CalCircumference(self):
		self.Circumference = 2 * self.PI * self.Radius

	def Display(self):
		print("Area of Circle 			: ",self.Area)
		print("Circumference of Circle 	: ",self.Circumference)


def main():
	
	obj_1 = Circle()

	obj_1.Accept()
	obj_1.CalculateArea()
	obj_1.CalCircumference()
	obj_1.Display()

	print("-----------------------------")

	obj_2 = Circle()

	obj_2.Accept()
	obj_2.CalculateArea()
	obj_2.CalCircumference()
	obj_2.Display()


if __name__ == '__main__':
	main()

