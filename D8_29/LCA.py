import sys
sys.setrecursionlimit(10**5)

v=int(input())
arr=[[] for i in range(v)]
for i in range(v-1):
    a,b=map(int,input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
s=int(input())
find=[[]for i in range(s)]
for i in range(s):
    a, b = map(int, input().split())
    find[i].append(a - 1)
    find[i].append(b - 1)
parents=[0 for i in range(v)]
d=[[] for i in range(v)]
visited = [None] * v
def dfs(v,depth):
    visited[v] = True
    d[v]=depth
    for w in arr[v]:
        if not visited[w]:
            parents[w]=v
            dfs(w,depth+1)
dfs(0,1)

def lca(a,b):
    while d[a] !=d[b]:
        if d[a]>d[b]:
            a=parents[a]
        else:
            b=parents[b]
    while(a!=b):
        a = parents[a]
        b = parents[b]
    print(a+1)
for i in find:
    lca(i[0],i[1])
