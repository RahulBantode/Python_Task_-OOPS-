'''Problem Statement :-
Write a Program which contains one class named as Demo. class contains two instance variables as no1,no2 .
That class contains one class variable as value.  There are two instance methods of class Fun() and Gun()
which displays values of instance variables.
Initialize instance variable in init method by accepting value from user
'''

class Demo:
	value = 10 								#class variable

	def __init__(self,num_1,num_2):			#Constructor of class
	 	self.val_1 = num_1 					#instance variable 1
	 	self.val_2 = num_2 					#instance variable 2


	def Fun(self):							#instance method
		return self.val_1

	def Gun(self):							#instance method
		return self.val_2

def main():

	no1 = int(input("Enter the number_1 : "))
	no2 = int(input("Enter the number_2 : "))
	print("--------------------------------------")
	obj = Demo(no1,no2)  #object of demo class is created....

	ret = obj.Fun()      
	print("Value return from <Fun> : ",ret)

	ret = obj.Gun()
	print("Value return from <Gun> : ",ret)

	print("--------------------------------------")
	print("Value of clas-variable : ",Demo.value)


if __name__ == '__main__':
	main()

