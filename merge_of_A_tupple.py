#+n=int(input("enter the size of tupple"))
tp=(1,2,3,4)
tp1=(5,6,7,8)
tp2=()
tp3=()
for i in range(len(tp)):
    tp2=(tp[i],tp1[i])
    tp3+=tp2,
print(tp3)
    
