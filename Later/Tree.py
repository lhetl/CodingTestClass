a=input()
sum=0
leftC=0
for i in range(len(a)):
    if a[i]=='(':
        if a[i+1]==')':
            sum+=leftC
        leftC += 1
    if a[i]==')':
        leftC-=1
print(sum)
