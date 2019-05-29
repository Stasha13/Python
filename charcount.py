word = 0 
msg = input("Enter any message")
search=input("What are you looking for?")
i=0
while i<len(msg):
	if (msg[i]) == search:
		word =word+1
	i=i+1
print ("There are", (word+1), "letter(s)")