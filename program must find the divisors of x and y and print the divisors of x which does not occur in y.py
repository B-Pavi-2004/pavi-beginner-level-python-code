x,y=map(int,input().split())
a=[]
b=[]
for i in range(1,x+1):
    if x%i==0:
        a.append(i)
for i in range(1,y+1):
    if y%i==0:
        b.append(i)
for i in a:
    if i not in b:
        print(i,end=" ")
