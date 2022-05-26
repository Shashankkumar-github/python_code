f=open("abc.txt")
s=f.readlines()
n = len(s)
print(n)
f.close()
f=open("abc.txt")
s1=f.read()
count=0;d=0
for ch in s1:
    if(ch.isalpha()):
        count+=1
    elif ch.isdigit():
        d+=1
cou=1
print(count,d)
for i in s1.split(' '):
    if(i==(' ')):
        cou+=1
print(cou)


