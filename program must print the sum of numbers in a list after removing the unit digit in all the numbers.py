lis=list(map(str,input().split()))
a=[]
for i in lis:
    b=int(i)/10
    a.append(b)
print(int(sum(a)))
