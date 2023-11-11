S=input()
a='aeiouAEIOU'
c1=c2=c3=0
for i in S:
    if i in a:
        c1+=1
        if i.isupper():
            c2+=1
        else:
            c3+=1
if c1==c2 or c1==c3:
    print("YES")
else:
    print("NO")
