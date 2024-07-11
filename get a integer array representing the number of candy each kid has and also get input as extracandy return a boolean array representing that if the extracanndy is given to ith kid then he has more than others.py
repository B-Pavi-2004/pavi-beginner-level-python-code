l1=list(map(int,input('candies=').split()))
ext=int(input('extraCandies='))
max=max(l1)
a=[]
for i in l1:
    tot=i+ext
    if tot>=max:
        a.append(True)
    else:
        a.append(False)
print(a)