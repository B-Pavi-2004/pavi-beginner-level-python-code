'''
----*
---**
--*-*-*
-*--*--*
*********
-*--*--*
--*-*-*
---***
----*
'''
N=int(input())
s=input()
n=N+(N-1)
c=N
k=-1
g=-1
for i in range(1,N+1):
    k+=1
    g+=1
    for j in range(1,n+1):
        if j==N or i==N or j==c-g or j==c+k:
            print(s,end="")
        elif j<c+k:
            print('-',end="")
        else:
            print(' ',end="")
    print()
c=1
d=n
k=0
g=0
for i in range(N-1,0,-1):
    k+=1
    g+=1
    for j in range(1,n+1):
        if j==N or i==N or j==d-k or j==c+g:
            print(s,end="")
        elif j<d-k:
            print('-',end="")
        else:
            print(' ',end="")
    print()
    


