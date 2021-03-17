'''Problem statement : 
   Design python application which creates three threads as small,capital,digits, all the threads accepts string as parameter. 
   Small thread display number of small characters, capital thread display number of capital characters.
   and digits thread will number of digits.
   display id and name of each thread.

'''
from threading import *
from os import *
from time import *

def small(kulup_lav,string="hiiRAHU983"):
	kulup_lav.acquire()
	print("PID of thread small : ",getpid()," : ",end=" ")
	for char in string:
		if char.islower():
			print(char,end=" ")

	print()
	kulup_lav.release()

def capital(kulup_lav,string="hiiRAHU983"):
	kulup_lav.acquire()
	print("PID of thread capital : ",getpid()," : ",end=" ")
	for char in string:
		if char.isupper():
			print(char,end=" ")

	print()
	kulup_lav.release()

def digits(kulup_lav,string="hiiRAHU983"):
	kulup_lav.acquire()
	print("PID of thread digits : ",getpid()," : ",end=" ")
	for digit in string:
		if digit.isdigit():
			print(digit,end=" ")

	print()
	kulup_lav.release()


def main():
	print("PID of main thread : ",getpid())

	kulup_lav = Lock()

	string = input("Enter the string ie (hiiRAHU983) ")
	t1 = Thread(target = small , args = (kulup_lav,string,))
	t2 = Thread(target = capital, args = (kulup_lav,string,))
	t3 = Thread(target = digits , args = (kulup_lav,string,))

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()

	print("thread operation are successful")

if __name__ == '__main__':
	main()

