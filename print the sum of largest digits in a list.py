lis=list(map(str,input().split()))
a=[]
b=[]
for i in lis:
    a=[]
    for j in i:
        a.append(int(j))
    b.append(max(a))
print(sum(b))
