'''Problem statement : 5
   design the python application which contains two threads named as thread_1,thread_2
   Thread_1 display 1 to 50 on screeen
   Thread_2 display 50 to 1  in reverse on screen
   After the execution of thread1 is completed thread_2 is scheduled
   means you have to synchronize the threads
 '''
from threading import *
from time import *


def ThreadOperation(func_name,kulup_Lav,no):
	func_name(kulup_Lav,no)

def Thread_1(kulup_lav,no):
 	kulup_lav.acquire()
 	i = 1
 	while i <= no:
 		print(i)
 		i = i+1
 		sleep(1)
 	kulup_lav.release()

def Thread_2(kulup_lav,no):
 	kulup_lav.acquire()
 	i = no
 	while i > 0:
 		print(i)
 		i = i-1
 		sleep(1)

 	kulup_lav.release()

def main():
 	kulup_lav = Lock()

 	no = int(input("Enter the value : "))

 	t1 = Thread(target = ThreadOperation , args = (Thread_1,kulup_lav,no,))
 	t2 = Thread(target = ThreadOperation , args = (Thread_2,kulup_lav,no,))

 	t1.start()
 	t2.start()

 	t1.join()
 	t2.join()

if __name__ == '__main__':
	main()

