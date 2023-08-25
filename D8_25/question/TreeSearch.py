from collections import deque
import sys
input = sys.stdin.readline
V=int(input())
E=V-1
resultArr=[[]for i in range(V)]
for i in range (E):
    a, b = map(int, input().split())
    resultArr[a-1].append(b-1)
    resultArr[b - 1].append(a - 1)
parents=[0 for i in range(V)]
parents[0]=1
def bfs(start):
    visit = [0 for i in range(V)]
    queue=deque()
    queue.append(start-1)
    visit[start-1]=1
    while len(queue)!=0:
        t=queue.popleft()
        for w in resultArr[t]:
            if visit[w]==0:
                parents[w]=t+1
                visit[w]=1
                queue.append(w)
bfs(1)
for i in parents[1:]:
    print(i)
