x,y=map(str,input().split())
li_1=list(map(str,input().split()))
sum1=0
for i in li_1:
    if i.endswith(y):
        sum1+=int(i)
print(sum1)
