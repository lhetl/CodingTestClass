N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))
ans=0
def chk(mid):
    money=0
    cnt=0
    for c in arr:
        if c>money:
            money=mid
            cnt+=1
        money -= c
    return cnt
low=max(arr)
high=sum(arr)
while low<=high:
    mid=(low+high)//2
    cnt=chk(mid)
    if cnt>M or mid<max(arr):
        low = mid+1
    else:
        high=mid-1
        ans=mid
print(ans)