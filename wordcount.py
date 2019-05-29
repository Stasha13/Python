def wordcount(message):
	word=1
	i=0
	while i<len(message):
		if message[i]==" ":
			word+=1
		i+=1
	return word


print ("No of words: ",wordcount("Hello my friend"))
print ("No of words: ",wordcount("i hate you my friend"))