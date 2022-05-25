x=int(input("enter first no."))
y=int(input("enter second no."))
z=int(input("enter third no."))
if(x>y):
    if(x<z):
        print("z is greater")
    else:
        print("x is greater")
elif(y<z):
    print("z is greater")
else:
    print("y is greater")                
