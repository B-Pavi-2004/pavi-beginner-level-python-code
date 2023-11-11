S1=input()
S2=input()
c=0
a=[]
for i in S1:
    if i in S2 and i not in a:
        c+=1
print(c)
