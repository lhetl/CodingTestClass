arr=[]
for i in range(9):
    arr.append(int(input()))
ans=[]
chk=[False for i in range(len(arr))]
tmp=[]
import sys
sys.setrecursionlimit(10**4)
def permNR(idx, N,R):
    if (R == idx) and sum(tmp)==100:
        tmp.sort()
        for i in tmp:
            print(i)
        exit(0)
    for i in range (N):
        if chk[i] == False:
            chk[i] = True
            tmp.append(arr[i])
            permNR(idx + 1, N, R)
            tmp.pop()
            chk[i] = False
permNR(0,9,7)