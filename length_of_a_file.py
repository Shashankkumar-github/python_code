f=open("abc.txt")
f.seek(0,2)
print(f.tell())
f.close()
