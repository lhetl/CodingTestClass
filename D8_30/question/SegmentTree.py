import sys
sys.setrecursionlimit(10**5)
N,searchCnt=map(int,input().split())
start = 1
while start < N:
    start *= 2
arr=[0 for i in range(start*2)]
arr2=[0 for i in range(start*2)]
#def.1
def update(pos):
    while pos != 0:
        arr[pos]=min(arr[pos*2],arr[pos*2+1])
        arr2[pos]=max(arr2[pos*2],arr2[pos*2+1])
        pos//=2

for i in range(N):
    v=int(input())
    pos=start+i
    arr[pos]=v
    arr2[pos]=v
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
def solveMax(idx,cl,cr,left,right):
    if left <= cl and cr <= right:
        return arr2[idx];
    if cr < left: return -sys.maxsize;
    if cl > right: return -sys.maxsize;
    mid = (cl + cr) // 2
    v1 = solveMax(idx * 2, cl, mid, left, right)
    v2 = solveMax(idx * 2 + 1, mid + 1, cr, left, right)
    return max(v1,v2)
for _ in range(searchCnt):
    a,b=map(int,sys.stdin.readline().split())
    print(solveMin(1,1,start,a,b),end=" ")
    print(solveMax(1, 1, start, a, b))