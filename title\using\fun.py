def cap(s):
    s1=str(s[0].upper())
    for i in range(1,len(s)):
        if s[i-1]==' ':
            s1+=s[i].upper()
            continue
        s1+=s[i]
    print(s1)
s=input()
cap(s)
