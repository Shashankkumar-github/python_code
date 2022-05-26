x=int(input("enter no."))
sum=0
while(x!=0):
    r=x%10
    sum=sum+r
    x=x//10
print(sum)
