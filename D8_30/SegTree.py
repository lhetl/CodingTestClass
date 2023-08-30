import sys
sys.setrecursionlimit(10**5)
N,updateCnt,plusCnt=map(int,input().split())
start = 1
while start < N:
    start *= 2
arr=[0 for i in range(start*2)]
#def.1
def update(pos):
    while pos != 0:
        arr[pos]=arr[pos*2]+arr[pos*2+1]
        pos//=2

for i in range(N):
    v=int(input())
    pos=start+i
    arr[pos]=v
    pos//=2
    update(pos)

#def2 nlogn
# for i in range(N):
#     v=int(input())
#     pos=start+i
#     while pos!=0:
#         arr[pos]+=v
#         pos//=2

# idx: 배열번호 cl,cr: 현재 왼쪽 오른쪽 left right : 질문 l,r
def solve(idx,cl,cr,left,right):
    if left <= cl and cr <= right:
        return arr[idx];
    if cr < left: return 0;
    if cl > right: return 0;
    mid = (cl + cr) // 2
    v1 = solve(idx * 2, cl, mid, left, right)
    v2 = solve(idx * 2 + 1, mid+1, cr, left, right)
    return v1 + v2;
for _ in range(updateCnt+plusCnt):
    a,b,c=map(int,input().split())
    if a==1:
        pos=start+b-1
        arr[pos]=c
        pos//=2
        update(pos)
    else:
        print(solve(1,1,start,b,c))
