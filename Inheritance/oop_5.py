#demonstration of inheritance.... Multiple inheritance

class Base_1:            
	def __init__(self):
		self.i = 10
		self.j = 20
		print("Inside the Base_1 Constructor")

class Base_2:			
	def __init__(self):
		self.x = 30
		self.y = 40
		print("Inside the Base_2 Constructor")

class Derived(Base_2,Base_1):   #and ethe Base_1,Base_2 or Base_2 , Base_1 ks hi dil tri sequence mater krt nhi
	def __init__(self):
		#ethe aapn jya sequence ne base class chya method la call kel tya pramane call jaiel
		Base_1.__init__(self) #explicitly call to Base_1 constructor
		Base_2.__init__(self) #explicitly call to Base_2 constructor
		self.a =39
		self.b =32
		print("Inside the Derived  Constructor ")

def main():
	d_obj = Derived()
	print(d_obj.i)
	print(d_obj.j)
	print(d_obj.x)
	print(d_obj.y)
	print(d_obj.a)
	print(d_obj.b)

if __name__ == '__main__':
	main()