alpha=input("Enter any character")

if ord(alpha)>=65 and ord(alpha)<=90:
	print ("Uppercase")
else:
	if ord(alpha)>=97 and ord(alpha)<=122:
		print ("Lowercase")
	else:
		if ord(alpha)>=48 and ord(alpha)<=57:
			print ("Digits")
		else:
			print ("Any other character")