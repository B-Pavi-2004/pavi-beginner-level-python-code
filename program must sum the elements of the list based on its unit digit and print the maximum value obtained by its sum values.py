n=int(input())
li_1=list(map(int,input().split()))
a=[]         
for i in li_1:
    sum1=0
    c=i%10
    for j in li_1:
        if j%10==c:
            sum1+=j
    a.append(sum1)
print(max(a))
        
        
    
