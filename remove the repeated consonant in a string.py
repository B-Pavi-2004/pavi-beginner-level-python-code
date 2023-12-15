S=input()
c=''
for i in S:
    if i.lower() not in c:
        print(i,end="")
        c+=1
