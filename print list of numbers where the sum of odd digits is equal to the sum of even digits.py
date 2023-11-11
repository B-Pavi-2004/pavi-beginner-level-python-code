N=int(input())
a='13579'
b=[]
sum1=sum2=0
for i in range(11,N+1,1):
    i=str(i)
    sum1=0
    sum2=0
    for j in i:
        if j in a:
            sum1+=int(j)
        else:
            sum2+=int(j)
    if sum1==sum2:
        b.append(i)
print(*b)
