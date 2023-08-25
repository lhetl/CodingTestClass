from collections import deque
import sys
input = sys.stdin.readline
V,E=map(int,input().split())
resultArr=[[]for i in range(V)]
for i in range (E):
    a, b = map(int, input().split())
    resultArr[b-1].append(a-1)
myque=deque()
countList=[0 for i in range(V)]
for j in range(V):
    myque.append(j)
    visitArr = [[False] for i in range(V)]
    visitArr[j] = True
    while len(myque)!=0:
        t=myque.popleft()
        for i in resultArr[t]:
            if(visitArr[i]==[False]):
                countList[j]+=1
                visitArr[i]=True
                myque.append(i)
maxVal=max(countList)
for i in range(V):
    if maxVal==countList[i]:
        print(i+1,end=" ")

