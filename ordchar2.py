alpha=input("Enter any character")

if ord(alpha)>=65 and ord(alpha)<=90:
	print (chr(ord(alpha)+32))
else:
	if ord(alpha)>=97 and ord(alpha)<=122:
		print (chr(ord(alpha)-32))
		