S=input()
a='qwrtyplkjhgfdszxcvbnm'
c=0
for i in a:
    if i not in S:
        c+=1
if c==0:
    print("YES")
else:
    print("NO")
