f=open("abc.txt")
n= int(input())
l=f.readlines()
[print(x) for x in l[-n:-1]]
f.close()
