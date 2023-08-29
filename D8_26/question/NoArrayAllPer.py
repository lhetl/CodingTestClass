N,M=map(int,input().split())
arr=[i+1 for i in range(N)]
ans=[]
tmp=[]
import sys
sys.setrecursionlimit(10**4)
def subSetNR(idx, N, R):
    if len(tmp) == R:
        for i in tmp:
            print(i,end=" ")
        print()
        return
    if idx == N:
        return
    for i in range(N):
        tmp.append(arr[i])
        subSetNR(idx + 1, N, R)
        tmp.pop()
subSetNR(0,N,M)