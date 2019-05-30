file_read=open("text.txt","r")
file_write=open("text2.txt","w")

for data in file_read:
	print (data, file=file_write)