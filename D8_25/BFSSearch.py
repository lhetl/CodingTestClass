from collections import deque
V,E=map(int,input().split())
resultArr=[[]for i in range(V)]
for i in range (E):
    a, b = map(int, input().split())
    resultArr[a-1].append(b)
    resultArr[b-1].append(a)
myque= deque()
firstNode = int(input())
myque.append(firstNode)
visitArr=[0 for i in range(V)]
visitArr[firstNode-1]=1
print(firstNode,end=": ")
cnt=0
while len(myque)!=0:
    t=myque.popleft()
    for i in resultArr[t-1]:
        if(visitArr[i-1]==0):
            print(i,end=" ")
            visitArr[i-1]=1
            myque.append(i)