import sys
input = sys.stdin.readline
u,v=map(int,input().split())
arr=[]
ans=[0]*v
for _ in range(u):
    arr.append(list(map(int,input().split())))
sumArr=[[0]*(u+1) for i in range(u+1)]
for i in range(1,u+1):
    for j in range(1,u+1):
        sumArr[i][j]=sumArr[i][j-1]+sumArr[i-1][j]-sumArr[i-1][j-1]+arr[i-1][j-1]
for n in range(v):
    x1,y1,x2,y2=map(int,input().split())
    ans[n]=sumArr[x2][y2]-sumArr[x1-1][y2]-sumArr[x2][y1-1]+sumArr[x1-1][y1-1]
print(ans)
for k in ans:
    print(k)