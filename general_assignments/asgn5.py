def area_rect():
	length =int(input("Enter the length  ="))
	breadth=int(input("Enter the breadth ="))
	result=length*breadth
	return result

def area_circle():
	pie=3.14
	radius=int(input("Enter the radius :"))
	result=pie*radius*radius
	return result

def area_triangle():
	length =int(input("Enter the length  ="))
	breadth=int(input("Enter the breadth ="))
	height =int(input("Enter the  height ="))
	result=length*breadth*height
	return result

rect=area_rect()
print("Area of rectangle =",rect,"\n")

cir=area_circle()
print("Area of circle =",cir,"\n")

tri=area_triangle()
print("Area of triangle =",tri,"\n")