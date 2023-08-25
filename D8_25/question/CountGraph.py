from collections import deque
import sys
input = sys.stdin.readline
V,E=map(int,input().split())
resultArr=[[]for i in range(V)]
for i in range (E):
    a, b = map(int, input().split())
    resultArr[a-1].append(b-1)
    resultArr[b-1].append(a-1)
myque= deque()
cnt=0
visitArr = [False for i in range(V)]
for i in range(V):
    if not visitArr[i]:
        myque.append(i)
        visitArr[i] = True
        cnt += 1
        while len(myque) != 0:
            t = myque.popleft()
            for i in resultArr[t]:
                if (visitArr[i] == False):
                    visitArr[i] = True
                    myque.append(i)
print(cnt)