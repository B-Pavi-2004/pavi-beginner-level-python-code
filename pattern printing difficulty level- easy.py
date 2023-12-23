r,c=map(int,input().split())
for i in range(1,r+1):
    for j in range(1,c+1):
        if i%2==0 and j%2==0:
            print('0',end="")
        else:
            print('*',end="")
    print()
