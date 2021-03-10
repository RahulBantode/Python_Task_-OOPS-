''' statement - wap which contains one function named as fun(). The function should display hello
			 	from function fun on console
'''

def fun():
	return "Hello I am from function <fun>"


def main():
	str = fun()
	print("The string : ",str)

if __name__ == '__main__':
	main()