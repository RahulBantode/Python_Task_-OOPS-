''' problem statement :-
	Design python application which creates two threads as evenlist and oddlist. Both the
	threads accept list of integers as parameters. 
	Evenlist thread add all even elements from input list and display the addition.
	Oddlist thread add all the odd elements from input list and display the addition.
'''

from threading import *
from time import *

def EvenList(arr,lock_lav):
	lock_lav.acquire()
	sum = 0

	for i in range(len(arr)):
		if arr[i] % 2 == 0:
			sum = sum + arr[i]
			#sleep(1)

	print("addition of evenlist : ",sum)
	lock_lav.release()

def OddList(arr,lock_lav):
	lock_lav.acquire()

	sum = 0

	for i in range(len(arr)):
		if arr[i] % 2 != 0:
			sum = sum + arr[i]
			#sleep(1)

	print("addition of oddlist : ",sum)
	lock_lav.release()

def main():
	lock_lav = Lock()

	size = int(input("Enter the size of the list : "))
	arr_list = []
	for i in range(size):
		arr_list.append(i)


	el = Thread(target = EvenList , args = (arr_list,lock_lav))
	ol = Thread(target = OddList , args = (arr_list,lock_lav))

	el.start()
	ol.start()

	el.join()
	ol.join()

	print("Execution comepleted...")

if __name__ == '__main__':
	main()


