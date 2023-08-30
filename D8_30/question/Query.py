import sys
sys.setrecursionlimit(10**5)
N=int(input())
start = 1
while start < N:
    start *= 2
arr=[0 for i in range(start*2)]
#def.1
def update(pos):
    while pos != 0:
        arr[pos]=min(arr[pos*2],arr[pos*2+1])
        pos//=2
v=list(map(int,input().split()))
for i in range(N):

    pos=start+i
    arr[pos]=v[i]
    pos//=2
    update(pos)

def solveMin(idx,cl,cr,left,right):
    if left <= cl and cr <= right:
        return arr[idx];
    if cr < left: return sys.maxsize;
    if cl > right: return sys.maxsize;
    mid = (cl + cr) // 2
    v1 = solveMin(idx * 2, cl, mid, left, right)
    v2 = solveMin(idx * 2 + 1, mid + 1, cr, left, right)
    return min(v1,v2)
searchCnt=int(input())
for _ in range(searchCnt):
    a, b, c = map(int, input().split())
    if a == 1:
        pos = start + b - 1
        arr[pos] = c
        pos //= 2
        update(pos)
    else:
        cnt=solveMin(1,1,start,b,c)
        mid=len(arr)//2
        for i in range(0,c+1-b):
            if arr[mid+b+i-1]==cnt:
                print(b+i)
                break