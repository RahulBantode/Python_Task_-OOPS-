'''Problem Statement
   Design the python application which creates a two thread named as even and odd.
   Even thread will display the first 10 even numbers. nd odd thread will display 
   the first 10 odd numbers.
'''

from threading import *
from time import *


def Operation(func_name,no):
	func_name(no)

def Thread_1(no):

	for i in range(no):
		if i % 2 == 0:
			print("even : ",i)
			sleep(1)

def Thread_2(no):

	for i in range(no):
		if i % 2 != 0:
			print("odd : ",i)
			sleep(1)


def main():
	no = 10
	
	t1 = Thread(target = Operation, args=(Thread_1,no,))
	t2 = Thread(target = Operation, args=(Thread_2,no,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("Operation successful")

if __name__ == '__main__':
	main()