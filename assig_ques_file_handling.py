f=open("d.txt",'w')
for i in range(50,501):
    f.write(str(i))
    f.write("\n")
f.close()
