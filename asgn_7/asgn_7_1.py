'''Problem statement :-
Write a program which contains one class named as BookStore.. BookStore class contains two variable
BookName,BookAuthor. That class contains one class variable as NoOfBooks which is initialize to 0
There is one instance methods of class as Display which display name, Author and number of books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method incremetn value of NoOfBooks by one.

After creating the class create the two objects of BookStore class as
Obj_1 =BookStore("LPI","Michale Keris");
Obj_1.Display //output as=  LPI by Michale Keris No. of books :1

Obj_2=BookStore("LSP","Robert Love");
Obj_2.Display //output as = LSP by Robert Love No. of books: 2 
'''

class BookStore:
	NoOfBooks = 0

	def __init__(self,BookName,BookAuthor):
		self.Bname   = BookName
		self.Bauthor = BookAuthor
		BookStore.NoOfBooks += 1 #to initalize class variable inside the init method syntax is 
								 #classname.classvariable for accessing it same syntax is followed

	def Display(self):
		print("{} by author {} , No of books : {}".format(self.Bname,self.Bauthor,BookStore.NoOfBooks))


def main():
	obj_1 = BookStore("Linux System Programming","Robert Love")
	obj_1.Display()

	obj_2 = BookStore("Linux Programming Interface","Michale Keris")
	obj_2.Display()

	obj_3 = BookStore("C Programming ","Dennis Ritchie")
	obj_3.Display()

	obj_4 = BookStore("Linux Implementation  ","Linus Torvalds")
	obj_4.Display()
	

if __name__ == '__main__':
	main()
