from collections import deque
n=int(input())
m=int(input())
arr2=[[]for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    arr2[a].append(b)
    arr2[b].append(a)
def BFS(start):
    visit=[0 for i in range(n+1)]
    queue=deque()
    queue.append([start,0])
    visit[start]=1
    ans=[0 for i in range(n+1)]
    while len(queue)!=0:
        t=queue.popleft()
        tPos=t[0]
        dis=t[1]
        for w in arr2[tPos]:
            if visit[w]==0:
                visit[w]=1
                ans[w]=dis+1
                queue.append([w,dis+1])
    cnt=0
    for v in ans:
        if v==1 or v==2:
            cnt+=1
    return cnt
print(BFS(1))