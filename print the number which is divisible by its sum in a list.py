lis=list(map(str,input().split()))
c=0
for i in lis:
    s=0
    for j in i:
        s+=int(j)

    if int(i)%s==0:
        print(i,end="")
        c+=1
if c==0:
    print("-1")
