lst=[(1,2),(3,4),(5,6)]
lst1=[(7,8),(9,10),(11,12)]
lst2=[]
for i in lst:
    for j in lst1:
        lst2.append(lst[i][j]+lst1[i][j])
print(lst2)
