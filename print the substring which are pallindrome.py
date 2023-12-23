s=input()
f=-1
for i in range(len(s)-2):
    if s[i]==s[i+2]:
        f=1
        print(s[i:i+3])
if f==-1:
    print(f)
