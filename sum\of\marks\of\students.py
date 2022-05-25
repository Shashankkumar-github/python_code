d={}
x=int(input("Enter the number of the students:"))
for i in range(x):
    roll=int(input("Enter the roll number of the srudents:"))
    d[roll]={}
    name=input("Enter the name of the students:")
    marks=[]
    for j in range(5):
        mark=int(input())
        marks.append(mark)
    d[roll].update({name:marks})
    print("The sum of the marks of the student is:%d"%sum(marks))
print(d)
