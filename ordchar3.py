msg=input("Enter any message")
char=0
i=0

while i<len(msg):
	if ord(msg)>=65 and ord(msg)<=90:
		print (chr(ord(msg)+32))
		word=char+1
	else:
		if ord(message)>=97 and ord(message)<=122:
			print (chr(ord(message)-32))
			word=char+1
		else:
			if ord(message)>=48 and ord(message)<=57:
				print (message*2)
				word=char+1
		i+=1