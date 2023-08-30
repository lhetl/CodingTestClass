
import sys
sys.setrecursionlimit(10**5)
testCnt=int(input())
def update(pos):
    while pos != 0:
        a=arr[pos*2]
        b=arr[pos*2+1]
        if a==0:
            a=sys.maxsize
        if b==0:
            b=sys.maxsize
        arr[pos]=min(a,b)
        pos//=2
def solve(idx,cl,cr,left,right):
    if left <= cl and cr <= right:
        return arr[idx];
    if cr < left: return sys.maxsize;
    if cl > right: return sys.maxsize;
    mid = (cl + cr) // 2
    v1 = solve(idx * 2, cl, mid, left, right)
    v2 = solve(idx * 2 + 1, mid+1, cr, left, right)
    return min(v1,v2)
for _ in range(testCnt):
    N, watchCnt = map(int, input().split())
    start = 1
    while start < N:
        start *= 2
    arr = [0 for i in range(start * 2)]
    for i in range(N):
        pos = start + i
        arr[pos] = i+1
        pos //= 2
        update(pos)
    watchList=list(map(int,input().split()))
    for i in range(1,watchCnt+1):
        cnt=solve(1,1,start,watchList[i-1],watchList[i-1]+1)
        print(cnt-1,end=" ")
        for j in range(watchList[i-1]):
            if arr[start+j]==cnt:
                change=start+j+1
                break
        for k in range(N):
            pos = start + k
            if arr[pos]<arr[change-1]:
                arr[pos] +=1
                pos //= 2
                update(pos)
        pos = change-1
        arr[pos] =1
        pos //= 2
        update(pos)
    print()