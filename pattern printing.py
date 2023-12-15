'''
%---%
---%-
--%--
-%---
%---%
'''
n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if (i==0 and (j==0 or j==n-1)) or (i==n-1 and (j==0 or j==n-1)) or (j==n-i-1):
            print("%",end="")
        else:
            print("-",end="")
    print()
