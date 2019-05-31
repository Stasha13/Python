def operations(day):
	if day==1:
		def fun(a,b):
			c=a+b
			print ("Result of addition: ", c)

	if day==2:
		def fun(a,b):
			c=a-b
			print ("Result of subtraction: ", c)

	return fun 

var=operations(2)
var(5,2)