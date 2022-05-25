lst=[(1,2),(3,4),(5,6)]
lst1=[(7,8),(9,10),(11,12)]
lst2=[]
tpl=()
for i in range(len(lst)):
    for j in range(len(lst1)):
        lst2.append(lst[i][0])
        lst2.append(lst1[i][0])
print(lst2)
a,b,c=1,2,3
