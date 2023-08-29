import heapq
import sys
v,e=map(int,input().split())
start=int(input())
start-=1
arr=[[]for i in range(v+1)]
for i in range(e):
    u1,u2,u3=map(int,input().split())
    u1-=1
    u2-=1
    arr[u1].append([u2,u3])
visit=[False]*(v)
ans=[sys.maxsize]*(v)
ans[start]=0
pq=[]
heapq.heappush(pq,[0,start])
while pq:
    t=heapq.heappop(pq)
    cost=t[0]
    pos=t[1]
    if visit[pos]==True:
        continue
    else:
        visit[pos]==True
    for w in arr[pos]:
        wPos=w[0]
        wc=w[1]
        if ans[wPos] > ans[pos]+ wc:
            ans[wPos]=ans[pos]+wc
            heapq.heappush(pq,[ans[wPos],wPos])
for i in ans:
    if(i==sys.maxsize):
        print("INF")
    else:
        print(i)