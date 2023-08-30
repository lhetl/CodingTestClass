import sys
sys.setrecursionlimit(10**2)
def f(x):
    idx1=sys.maxsize
    idx2=sys.maxsize
    idx3=sys.maxsize
    if x==1:
        return 0
    if x in memo.keys():
        return memo[x]

    if x%3==0:
        idx1=f(x//3)
    if x%2==0:
        idx2=f(x//2)
    if x%2!=0 or x%3!=0:
        idx3=f(x-1)

    memo[x]= min(idx1,idx2,idx3)+1
    return memo[x]
n=int(input())
memo={1:0}
print(f(n)-1+1)