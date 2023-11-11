S=input()
value=''
c=0
for i in range(len(S)):
    a=S[len(S)-1-c:]
    value+=a
    c+=1
print(value)
