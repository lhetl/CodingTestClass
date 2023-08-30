def f(x):
    if memo[x] != None:
        return memo[x]
    if x == 2:
        return 2
    if x == 1:
        return 1
    if x==0:
        return 1
    memo[x] = f(x-1)+f(x-2)+f(x-3)
    return memo[x]


n=int(input())

for i in range(n):
    m=int(input())
    memo = [None for i in range(m + 1)]
    print(f(m))