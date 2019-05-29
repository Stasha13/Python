product = input("Enter product name")
price = input("Enter price")
quantity = input("Enter quantity")
amount = float(price)*int(quantity)
vat = amount*15/100
bill = amount + vat
print ("---------------------------")
print ("Your bill")
print (product)
print (amount)
print (vat)
print (bill)
print ("---------------------------")
