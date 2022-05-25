def perfect(n):
    sum=0
    for i in range(1,n//2+1):
        if(n%i==0):
            sum =sum+i
    return sum

x=int(input())
if(perfect(x)==x):
    print("a perfect number")
else:
    print("not a pefect number")    
