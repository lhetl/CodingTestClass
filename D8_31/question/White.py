def check(a,b):
    if a%2==b%2:
        return 1
    else:
        return 0
arr=[[0 for i in range (8)] for j in range(8)]
cnt=0
for i in range(8):
    length=input()
    for j in range(len(length)):
        if length[j]=="F":
            cnt+=check(i,j)
            arr[i][j]=1
print(cnt)