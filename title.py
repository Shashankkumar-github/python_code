def title(s):
    for x in s[:].split():
        s=s.replace(s,s.capitalize())
    return s
x=input()
print(title(x))
