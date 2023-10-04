
n=int(input())
numList=list(map(int,input().split()))
cnt=0
for j in numList:
    check=True
    for i in range(2,int(j**0.5)+1,1):
        if j%i==0:
            check=False
            break
    if check==True and j!=1:
        cnt += 1
print(cnt)