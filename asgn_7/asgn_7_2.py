'''Problem Statment :
WAP which has one class with named as BankAccount. BankAccount class contains two instance variables
as Name and Amount. That class contains one classs variable as ROI which initalise to 10.5
Inside the init method initialise all name and amount variables by accepting the values from user.
There are four instances methods inside the class as Display(), Deposite(), Withdraw(),CalculateInterest().
Deposite() - this method accept the amount from user and add that value in class instance variable Amount
Withdraw() - this method accept the amount to be withdrawn from user. and substract that amount from class inst
			 instance variable.
CalculateInterest :- this method calculate the interest based on Amount by considering rate of interest
					 which is class variable as ROI

Display() :- This method will display value of all instance variables as Name and Amount

After designing the above class call all instancess methods by creating multiple objects.

'''

class BankAccount:
	ROI = 10.5 #class variable Rate of Interest

	def __init__(self):
		self.Name = ""
		self.Amount = 0

	def AcceptDetails(self):
		self.Name = input("Enter Account holder name : ")
		self.Amount = int(input("Initial amount in account : "))

	def Deposite(self):
		amt = int(input("Enter the amount to deposite : "))
		self.Amount = self.Amount + amt

	def Withdrawn(self):
		widrw = int(input("Enter the amount to withdrawn : "))
		self.Amount = self.Amount - widrw

	def CalculateInt(self):
		interest = BankAccount.ROI / 100 * self.Amount
		return interest

	def Display(self):
		print("Account Holder name             : ",self.Name)
		print("Balance remains     			   : ",self.Amount)
		print("current interest on your amount : ",self.CalculateInt())

def main():

	obj_1 =BankAccount()	
	obj_1.AcceptDetails()
	obj_1.Deposite()
	obj_1.Withdrawn()
	obj_1.Display()
	print("---------------------------------------------")

	obj_2 =BankAccount()	
	obj_2.AcceptDetails()
	obj_2.Deposite()
	obj_2.Withdrawn()
	obj_2.Display()
	print("---------------------------------------------")


	obj_3 =BankAccount()	
	obj_3.AcceptDetails()
	obj_3.Deposite()
	obj_3.Withdrawn()
	obj_3.Display()
	print("---------------------------------------------")

if __name__ == '__main__':
	main()
