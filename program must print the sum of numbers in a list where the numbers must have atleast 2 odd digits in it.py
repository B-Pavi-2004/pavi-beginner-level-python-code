lis=list(map(str,input().split()))
c=0
sum1=0
a='13579'
for i in lis:
    c=0
    for j in i:
        if j in a:
            c+=1
    if c>=2:
        sum1+=int(i)
print(sum1)
