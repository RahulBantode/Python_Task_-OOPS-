#Demonstration of access specifier
#access specifier means its concept of making a restrictions on the class behaviors or characters
#		of the class.
''' 
In python there is no keyword like private , protected, public 
we can achieve it by symboling to variables, and methods
like,

public variable    =  obj.varname
protected variable =  obj._varname
private variable   =  obje.__varname

public method    = obj.methodname
protected method = obj._methodname
private method   = obj.__methodname

'''
class Base:
	no = 200     #class variable as public
	_no = 300    #class variable as protected
	__no = 100   #class variable as private

	def __init__(self):
		self.no1 = 11 #public
		self._no2 = 23 #protected
		self.__no3 = 34 #private

	def fun(self):     #public method
		print(self.no1,self._no2,self.__no3)
		self.__fun()   #it is private function so it is accessible in the base class.

	def _fun(self):		#protected method
		print(self.no1,self._no2,self.__no3)

	def __fun(self):	#private method
		print("Inside the private function")


class Derived(Base):
	
	print(Base.no)
	print(Base._no)
	# print(Base.__no)		it is not allowed becuase it is private class....

	def __init__(self):
		Base.__init__(self)  #its good way of programming that called the init method of base class
							 #inside the init method of derived class.

	def gun(self):
		print(self.no1)
		print(self._no2)
		#print(self.__no3)       private member not allowed / or not inherited to derived class
		self.fun()
		self._fun()
		#self.__fun()			private method not allowd/ or not inherited to derived class

class ddd(Derived):

	def __init__(self):
		Derived.__init__(self)
		print(self.__no2) #its protected define in base class which are accesssible in intermediate derived class
						  #it is not intermediate derived class of base class
						  #so it is not accessible. 

def main():

	obj1 = Base()
	print(obj1.no1)
	print(obj1._no2)
	#print(obj1.__no3)		--not allowed because it is private variable.
	obj1.fun()
	obj1._fun()
	#obj1.__fun()			--not allowed because it is private method

	obj2 = Derived()
	obj2.gun()

	ob = ddd()
if __name__ == '__main__':
	main()