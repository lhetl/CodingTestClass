u,v=map(int,input().split())
arr=list(map(int,input().split()))
ans=[0 for i in range(v)]
sumArr=[0 for i in range(u+1)]
for i in range(u):
    sumArr[i+1]=sumArr[i]+arr[i]
for i in range(v):
    a,b=map(int,input().split())
    ans[i]=sumArr[b]-sumArr[a-1]
for i in ans:
    print(i)