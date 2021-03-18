#demonstration of inheritance.... Multiple inheritance

class Base_1:            
	def __init__(self):
		print("Inside the Base_1 Constructor")

	def fun(self):
		print("Base_1 method")

class Base_2:			
	def __init__(self):
		print("Inside the Base_2 Constructor")


	def fun(self):
		print("Base_2 method")

class Derived(Base_2,Base_1):  #here order of inheriting the base class is matter,becz both base class 
							   #have same function name.
	def __init__(self):
		#ethe aapn jya sequence ne base class chya method la call kel tya pramane call jaiel
		Base_2.__init__(self) #explicitly call to Base_1 constructor
		Base_1.__init__(self) #explicitly call to Base_2 constructor
		
		print("Inside the Derived  Constructor ")

	def fun(self):
		print("Derived fun ") #ethe Fun method which are comes from base class are overried because Fun method
		                      #Derived class mdhe aahe so derived class chi fun method call hoiel.

def main():
	d_obj = Derived()
	d_obj.fun() #same fun method 2ni base class mdhe asli tr inherite krtana konta base class pahile
				#inherit kelay tyatli method call hoiel (Base_1,Base2)
				#ethe Base_1 chi fun method
				#jr (Base_2,Base_1)
				#ethe Base_2 chi fun method

if __name__ == '__main__':
	main()