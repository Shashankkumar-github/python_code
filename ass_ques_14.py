f=open("C:\\Users\\RAJ\\abc.txt",'r')
f1=open("C:\\Users\\RAJ\\xyz.txt",'r')
for i,j in zip(f,f1):
    i=i.strip()
    j=j.strip()
    print(i+j)
f.close()
f1.close()



