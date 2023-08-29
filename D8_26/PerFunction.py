arr=[] #주어진 데이터
chk=[] #선택 유무 학인
tmp=[] #선택 중 임시 보관용(현재 고른상태)
ans=[] #결과 출력용
idx=0 # 순열 깊이
N=0 # 데이터수
r=0 # 순열 길이
def permAll(idx, N): #데이터로 모든 순열 만들기
    if N == idx:
        ans.append(tmp[:])
        return
    for i in range(N):
        if chk[i] == False:
            chk[i] = True
            tmp.append(arr[i])
            permAll(idx+1, N)
            tmp.pop()
            chk[i] = False # 중복 생성 O
def permNR(idx, N,R): #N개 중 R개를 고른 후 순열 만들기
    if R == idx:
        ans.append(tmp[:])
        return
    for i in range (N):
        if chk[i] == False:
            chk[i] = True
            tmp.append(arr[i])
            permNR(idx + 1, N, R)
            tmp.pop()
            chk[i] = False
n,r=map(int,input().split())
def rec(depth): #중복체크 X
    if depth==r:
        return
    for i in range(n):
        rec(depth+1)


def subSet(idx, N): #공집합 포함 생성 (1,2,3,12,13,123)
    if idx == N:
        ans.append(tmp[:])
        return
    chk[idx] = True
    tmp.append(arr[idx])
    subSet(idx + 1, N)
    tmp.pop()
    chk[idx] = False
    subSet(idx+1,N)
    
import sys
sys.setrecursionlimit(10**4)

def subSetNR(idx, N, R):
    if len(tmp) == R:
        ans.append(tmp[:])
        return
    if idx == N:
        return
    chk[idx] = True
    tmp.append(arr[idx])
    subSetNR(idx + 1, N, R)
    tmp.pop()
    chk[idx] = False
    subSetNR(idx+1,N, R)