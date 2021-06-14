def area_rect(length, breadth,height=3):
	result=length*breadth*height
	return result

br=int(input("Enter the br"))

area=area_rect(2,br)
print("Area of Rectangle =",area)

''' program for default argument giving to function

and most important

def area_rect(length=5,breadth):

	this will give an error as non-default argument follows
	default argument

	because value assignment is left to right then compiler
	get confuse to assignment if you give first para as 
	default args. and second is not... so assign default args
	in left to right if you give the left args as default
	args. then rest of the all right to this args given as default
	args


def fun_n(n):
	pass

fun_n(2,3)

this will give an error--
fun_n() takes 1 positional argument but 2 were given'''