try:
	number1 = int(input("Enter first number"))
	number2 = int(input("Enter second number"))
	result = number1/number2
	print ("The answer is: ", result)

except ValueError:
	print("Please only enter numbers")

except ZeroDivisionError: 
	print ("System cannot divide by zero")

except Exception:
	print ("Something went wrong")