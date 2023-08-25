from collections import deque
import sys
input = sys.stdin.readline
V=int(input())
search,find=map(int,input().split())
E=int(input())
resultArr=[[]for i in range(V)]
for i in range (E):
    a, b = map(int, input().split())
    resultArr[a-1].append(b-1)
    resultArr[b - 1].append(a - 1)

cntList=[]
def bfs(start):
    visit = [0 for i in range(V)]
    queue=deque()
    queue.append(start-1)
    visit[start-1]=1
    while len(queue)!=0:
        t=queue.popleft()
        for w in resultArr[t]:
            if visit[w]==0:
                visit[w]=1
                print(w + 1, end=" ")
                bfs(w)
        if t == find - 1:
            return cnt-1
    return -1
print(bfs(search))