s=input()
x,y=map(str,input().split())
for i in s:
    if i==x:
        print('a',end="")
    else:
        print('b',end="")
