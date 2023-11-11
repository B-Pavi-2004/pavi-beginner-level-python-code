S=input()
j=0
for i in range(len(S)):
    if i>0:
        j=0
        while(j<i):
            print(S[i],end="")
            j+=1
    value=S[i:]
    print(value)
