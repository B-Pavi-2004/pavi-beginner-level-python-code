N=input()
a=[]
s1=int(N[:-1])
s2=int(N[:-2]+N[-1])
s3=int(N[:-3]+N[-2]+N[-1])
a.append(s1)
a.append(s2)
a.append(s3)
print(min(a))
