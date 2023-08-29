N,M=map(int,input().split())
arr=[i+1 for i in range(N)]
ans=[]
chk=[False for i in range(len(arr))]
tmp=[]
import sys
sys.setrecursionlimit(10**4)
def permNR(idx, N,R): #N개 중 R개를 고른 후 순열 만들기
    if R == idx:
        for i in tmp[:]:
            print(i,end=" ")
        print()
    for i in range (N):
        if chk[i] == False:
            chk[i] = True
            tmp.append(arr[i])
            permNR(idx + 1, N, R)
            tmp.pop()
            chk[i] = False
permNR(0,N,M)