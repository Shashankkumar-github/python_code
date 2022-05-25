def calc(n,m):
    a=n+m
    b=n-m
    c=n*m
    d=n//m
    return a,b,c,d

x=int(input())
y=int(input())
k,l,m,n = calc(x,y)
print(k,l,m,n)
