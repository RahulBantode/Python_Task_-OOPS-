'''Problem Statement:-
   Design the python application which creates two threads as evenfactor and oddfactor,
   Both the thread accept one parameter as integer. 
   Evenfactor thread will display addition of even factors
   OddFactor thread will display addition of odd factors of given numbers.
   After execution both the thread gets completed main thread should display messege as exit from main.

'''
from threading import *
from time import *

def EvenFactor(no):
	for i in range(1,no):
		if no % i == 0:
			if i % 2 == 0:
				print("evenfactor :",i)
				sleep(1)	

def OddFactor(no):
	for i in range(1,no):
		if no % i == 0:
			if i % 2 != 0:
				print("OddFactor : ",i)
				sleep(1)

def main():
	no = int(input("Enter the number : "))

	ef = Thread(target = EvenFactor , args = (no,))
	of = Thread(target = OddFactor  , args = (no,))

	ef.start()
	of.start()

	ef.join()
	of.join()

	print("thread execution are completed ")


if __name__ == '__main__':
	main()