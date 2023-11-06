n,b,a=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
tmp=0
cnt=0
checkArr=[False for i in range(n)]
for i in range(n):
    if tmp+arr[i] <= b:
        tmp+=arr[i]
        cnt=i+1
    else:
        check = False
        for j in range(i,-1,-1):
            if checkArr[j]: continue
            if(a==0): break
            tmp-=arr[j]//2
            a-=1
            checkArr[j]=True
            if tmp+arr[i] <=b:
                check=True
                tmp+=arr[i]
                cnt=i+1
                break
        if not check:
            break
print(cnt)