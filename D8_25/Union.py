import sys
sys.setrecursionlimit(100000)
n,m=map(int,input().split())
p=[]
for i in range(n+1):
    p.append(i)
def findSet(x):
    if x== p[x]:
        return x
    p[x]=findSet(p[x])
    return findSet(p[x])
def union(a,b):
    pa=findSet(a)
    pb=findSet(b)
    p[pa]=pb
for i in range(m):
    a,b,c=map(int,input().split())
    if a==0:
        union(b,c)
    elif a== 1:
        if findSet(b)==findSet(c):
            print("YES")
        else:
            print("NO")