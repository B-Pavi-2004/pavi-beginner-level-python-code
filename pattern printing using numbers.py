'''
44444444
33331111
22222222
13131313
'''
n=int(input())
a=n*2
k=1
for i in range(n,0,-1):
    for j in range(1,n*2+1):
        if j<=a//2:
            print(i,end="")
        else:
            print(k,end="")
    k+=1
    print()
        
