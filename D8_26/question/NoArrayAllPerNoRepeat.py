N,M=map(int,input().split())
arr=[i+1 for i in range(N)]
ans=[]
tmp=[]
import sys
sys.setrecursionlimit(10**4)
def subSetNR(idx, N, R):
    if len(tmp) == R:
        ans.append(tmp[:])
        return
    if idx == N:
        return
    for i in range(N):
        if len(tmp) != 0:
            if i+1>=tmp[idx-1]:
                tmp.append(arr[i])
                subSetNR(idx + 1, N, R)
                tmp.pop()
        elif len(tmp) ==0:
            tmp.append(arr[i])
            subSetNR(idx + 1, N, R)
            tmp.pop()
subSetNR(0,N,M)

for i in ans:
    for j in i:
        print(j,end=" ")
    print()