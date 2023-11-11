N=int(input())
lis=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in range(1,N+1):
    if N%i==0:
        a.append(i)
for i in a:
    if i not in lis:
        b.append(i)
c=b.sort(reverse=True)
print(*b)
