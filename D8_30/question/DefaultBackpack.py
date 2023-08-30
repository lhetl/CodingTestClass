v,e=map(int,input().split())
objectList=[]
for i in range(v):
    objectList.append(list(map(int,input().split())))
dp=[[0 for i in range (e+1)] for i in range(v+1)]
dp[0][0]=0
for i in range(1,v+1):
    for j in range(1,e+1):
        w=objectList[i-1][0]
        c=objectList[i-1][1]
        if w>j:
            dp[i][j]=dp[i - 1][j]
        else:
            dp[i][j]=max(dp[i - 1][j -w] + c, dp[i-1][j])
print(dp[v][e])