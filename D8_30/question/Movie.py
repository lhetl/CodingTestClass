import sys
from math import ceil,log
sys.setrecursionlimit(10**5)
testCnt=int(input())
def mid(a,b):
    return (a+b)//2
def init(l, r, node):
    if l == r:
        arr[node] = arr2[l]
        return
    init(l, mid(l,r), node*2)
    init(mid(l,r)+1, r, node*2+1)
    arr[node] = arr[node*2] + arr[node*2+1]

def update(l, r, node, IDX, DIFF):
    if not (l <= IDX <= r):
        return
    arr[node] += DIFF
    if l == r:
        return
    update(l, mid(l,r), node*2, IDX, DIFF)
    update(mid(l,r)+1, r, node*2+1, IDX, DIFF)
def solve(idx,cl,cr,left,right):
    if left <= cl and cr <= right:
        return arr[idx];
    if cr < left: return 0;
    if cl > right: return 0;
    mid = (cl + cr) // 2
    v1 = solve(idx * 2, cl, mid, left, right)
    v2 = solve(idx * 2 + 1, mid+1, cr, left, right)
    return v1+v2
for _ in range(testCnt):
    N, watchCnt = map(int, input().split())
    start = 1
    while start < N:
        start *= 2
    arr= [0] * (2**ceil(log(N+watchCnt, 2)+1))
    pos = [0] + [i + watchCnt for i in range(N)]
    arr2= [0] * watchCnt + [1] * N
    init(0,N+watchCnt-1,1)
    watchList=list(map(int,input().split()))
    last=watchCnt-1
    print(arr)
    for i in watchList:
        maxLen=N+watchCnt-1

        update(0, maxLen, 1, pos[i], -1)
        print(solve(1,0, maxLen, 0, pos[i] - 1), end=' ')
        pos[i] = last
        last -= 1
        update(0, maxLen, 1, pos[i], +1)
    print()