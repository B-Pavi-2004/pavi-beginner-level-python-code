N=int(input())
li_1=list(map(int,input().split()))
sum1=[]
b=[]
c=0
for k in range(0,len(li_1),3):
    b=li_1[k:k+3]
    c=sum(b)
    sum1.append(c)
print(min(sum1))
