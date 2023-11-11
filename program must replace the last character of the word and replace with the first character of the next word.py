S=input()
for i in range(len(S)-1):
    if S[i+1]!=' ':
        print(S[i],end="")
    else:
        print(S[i+2],end="")
print(S[0],end="")
