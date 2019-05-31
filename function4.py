def subtraction(x,y):
	c=x-y
	print ("Result of subtraction: ",c)

def addition(a,b):
	c=a+b
	print ("Result of addition: ",c)

def operation(f,a,b):
	f(a,b)

operation(addition,10,20)
operation(subtraction,50,50)