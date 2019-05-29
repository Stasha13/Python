name = input("Enter your name")
salary = (int(input("Enter your salary")))
if salary > 20000:
	tax = salary*25/100
else:
	tax = salary*15/100
netsalary = salary-tax
print ("Name:",name)
print ("Salary:",salary)
print ("Tax",tax)
print ("Net salary",netsalary)