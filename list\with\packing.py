lst=[(1,2),(3,4),(5,6)]
lst1=[(7,8),(9,10),(11,12)]
# print [(1,2),(11,12)] amd lst3=[(1,12)]
lst3=[]
n1,*n2=lst
*n3,n4=lst1
lst2=[n1,n4]
print(lst2)
lst3.append(lst[0][0])
lst3.append(lst1[2][1])
print(lst3)
