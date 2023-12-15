N=int(input())
li=list(map(str,input().split()))
a=[]
for i in li:
    c=0
    for j in i:
        if i.count(j)==len(i):
            c+=1
    if c!=0:
        a.append(i)
if len(a)==0:
    print("-1")
else:
    print(*a)
