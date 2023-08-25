from collections import deque
v,e=map(int,input().split())
arr2=[[]for i in range(v)]
for i in range(e):
    a,b=map(int,input().split())
    arr2[a-1].append(b-1)
    arr2[b-1].append(a-1)
def bfs(start):
    visit = [0 for i in range(v)]
    queue=deque()
    queue.append(start-1)
    visit[start-1]=1
    print(start,end=": ")
    while len(queue)!=0:
        t=queue.popleft()
        for w in arr2[t]:
            if visit[w]==0:
                visit[w]=1
                print(w+1,end=" ")
                queue.append(w)
bfs(1)

