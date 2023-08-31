from collections import deque
v,e,start=map(int,input().split())
arr2=[[]for i in range(v)]
for i in range(e):
    a,b=map(int,input().split())
    arr2[a-1].append(b-1)
    arr2[b-1].append(a-1)
for i in arr2:
    i=i.sort()
ansB=[]
ansD=[]
def bfs(start):
    visit = [0 for i in range(v)]
    queue=deque()
    queue.append(start-1)
    visit[start-1]=1
    ansB.append(start)
    while len(queue)!=0:
        t=queue.popleft()
        for w in arr2[t]:
            if visit[w]==0:
                visit[w]=1
                ansB.append(w+1)
                queue.append(w)

visited = [False for i in range(v)]
def dfs(v):
    visited[v] = True
    ansD.append(v+1)
    for w in arr2[v]:
        if not visited[w]:
            dfs(w)

bfs(start)
dfs(start-1)
for i in ansD:
    print(i,end=" ")
print()
for i in ansB:
    print(i,end=" ")
