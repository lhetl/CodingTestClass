import sys
sys.setrecursionlimit(10**4)
def f(x):
    if memo[x] != None:
        return memo[x]
    if x == 2:
        return 3
    if x == 1:
        return 1
    if x==0:
        return 1
    memo[x] = f(x-1)+(f(x-2)*2)
    return memo[x]


n=int(input())
memo = [None for i in range(n + 1)]
print(f(n)%10007)