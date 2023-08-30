def f(x):
    if memo[x] != None:
        return memo[x]
    if x == 2:
        return w[1] + w[2]
    if x == 1:
        return w[1]
    if x==0:
        return 0
    memo[x] = max(f(x - 2) + w[x], f(x - 3) + w[x] + w[x - 1])
    return memo[x]


n=int(input())
w=[0]
for i in range(n):
    w.append(int(input()))
memo=[None for i in range(n+1)]
print(f(n))