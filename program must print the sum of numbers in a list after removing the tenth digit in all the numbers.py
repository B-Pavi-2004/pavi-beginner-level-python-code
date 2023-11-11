lis=list(map(str,input().split()))
a=[]
for i in lis:
    b=i[:-2]+i[-1]
    a.append(int(b))
print(sum(a))
