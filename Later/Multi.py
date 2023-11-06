import sys
n=int(input())
arr=[]
ans=[[] for i in range(n)]

def f(left,right,bel,ber):
    if ans[left][right]!=-1:
        return
    else:
        cnt=ans[bel][ber]+arr[left][0]*arr[right][0]*arr[right][1]

    if ans[left][right]>cnt:
        ans[left][right]=cnt
    if left>0:
        f(left-1,right,left,right)
    if right<n-1:
        f(left,right+1,left,right)
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        ans[i].append(sys.maxsize)
for i in range(n-1):
    ans[i][i+1]=arr[i][0]*arr[i+1][0]*arr[i+1][1]
    f(i,i+1,i,i+1)
for i in ans:
    print(i)
print(ans[0][n-1])
