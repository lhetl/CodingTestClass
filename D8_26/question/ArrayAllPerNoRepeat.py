N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
ans=[]
chk=[False for i in range(len(arr))]
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
        if len(tmp) != 0:
            if arr[i] >= tmp[idx - 1]:
                tmp.append(arr[i])
                subSetNR(idx + 1, N, R)
                tmp.pop()
        elif len(tmp) == 0:
            tmp.append(arr[i])
            subSetNR(idx + 1, N, R)
            tmp.pop()
subSetNR(0,N,M)