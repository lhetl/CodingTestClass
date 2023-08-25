from collections import deque
V=int(input())
E=int(input())
resultArr=[[]for i in range(V)]
for i in range (E):
    a, b = map(int, input().split())
    resultArr[a-1].append(b)
    resultArr[b-1].append(a)
myque= deque()
firstNode = 1
myque.append(firstNode)
visitArr=[0 for i in range(V)]
visitArr[firstNode-1]=1
cnt=0
while len(myque)!=0:
    t=myque.popleft()
    for i in resultArr[t-1]:
        if(visitArr[i-1]==0):
            cnt+=1
            visitArr[i-1]=1
            myque.append(i)
print(cnt)