f=open("C:\\Users\\RAJ\\d.txt",'w+')
for i in range(50,500):
    s=f.write(str(i)+'\n')
f.close()
f=open("C:\\Users\\RAJ\\d.txt",'r')
s=f.read()
print(s)
f.close()

