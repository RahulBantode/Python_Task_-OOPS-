#demonstration of inheritance.... Multilevel inheritance

class Base:            
	def __init__(self):
		self.i = 10
		self.j = 20
		print("Inside the Base Constructor")

class Derived_1(Base):			
	def __init__(self):
		Base.__init__(self)   #explicitly call to base class __init__ method
		self.x = 30
		self.y = 40
		print("Inside the Derived 1 Constructor")

class Derived_2(Derived_1):   #explicitly call to Derived_1 class __init__ method
	def __init__(self):
		Derived_1.__init__(self)
		self.a =39
		self.b =32
		print("Inside the Derived 2 Constructor ")

def main():
	d_obj = Derived_2()
	print(d_obj.i)
	print(d_obj.j)
	print(d_obj.x)
	print(d_obj.y)
	print(d_obj.a)
	print(d_obj.b)

if __name__ == '__main__':
	main()