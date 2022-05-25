def strong(n):
    n1=n
    t=0
    while(n>0):
        d=n%10
        f=1
        for i in range(1,d+1):
            f=f*i
        t=t+f
        n=n//10
    return t
n=int(input())
if(strong(n)==n):
    print("strong")
else:
    print("not")
