#demonstration of inheritance....
#single level inheritance

class Base:
	def __init__(self):
		self.i = 10
		self.j = 20
		print("Inside the Base Constructor")

	def Fun(self):
		print("Inside the Base class <Fun> instance method")

	def Gun(self):
		print("Inside the Base class <Gun> instance method")


class Derived(Base):
	def __init__(self):
		Base.__init__(self)   #explicitly call to base class __init__ method
		self.x = 30
		self.y = 40
		print("Inside the Derived Constructor")

	def Sun(self):
		print("Inside the Derived class <Sun> instance method")

	def Gun(self):   #compiler ethe base class chya method la override kel tyane derived class chya object mule
					#derived class chi gun method call jhali
		Base.Gun(self) #by using this we can access it...
		print("Inside the Derived class <Gun> instance method")



def main():
	d_obj = Derived()
	print(d_obj.i)
	print(d_obj.j)
	print(d_obj.x)
	print(d_obj.y)

	d_obj.Sun()
	d_obj.Gun()
	d_obj.Fun()


if __name__ == '__main__':
	main()