s1=input()
s2=input()
a=s1.lower()
b=s2.lower()
ai=''
for i in range(len(a)):
    if b[i]=='u':
        ai+=a[i].upper()
    else:
        ai+=a[i].lower()
print(ai)
