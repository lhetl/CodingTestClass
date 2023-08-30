import sys
sys.setrecursionlimit(10**5)

def f(x,idx):
    idx1=sys.maxsize
    idx2=sys.maxsize
    if x<=1:
        ans.append(idx)
        return idx
    if memo[x-1] != sys.maxsize:
        return memo[x]
    if x%3==0 and x//3>=1:
        idx1=f(x//3, idx + 1)
    if x%2==0 and x//2>=1:
        idx2=f(x//2, idx + 1)

    idx3=f(x-1, idx + 1)
    memo[x-1]= min(memo[x-1],idx1,idx2,idx3)
    return memo[x-1]+1
    # memo[x]=min(f(cnt1,idx+1),f(cnt2,idx+1),f(x-1,idx+1))
    # return idx
n=int(input())
memo=[sys.maxsize for i in range(n)]
memo[0]=1
ans=[]
print(f(n,0))
print(ans)