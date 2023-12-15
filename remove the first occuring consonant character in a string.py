S=input()
c=''
s=S[::-1]
a='aeiouAEIOU'
for i in s:
    if i in a:
        c+=i
    elif i not in c:
        c+=i
print(c[::-1])

