n=int(input())
b=str(bin(n))[2:]
cr=''
count=0
val=0
k=0
print(b)
rb=b[::-1]
print(rb)
for i in rb:
    if i=='1' and count==0:
        cr+='0'
        count=1
    else:
        cr+=i
print(cr)
rcr=cr[::-1]
print(rcr)
bn=int(rcr)
while bn!=0:
    u=bn%10
    val=val+u*pow(2,k)
    bn//=10
    k+=1
print(val)



