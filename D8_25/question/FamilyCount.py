import sys
input = sys.stdin.readline
V=int(input())
search,find=map(int,input().split())
E=int(input())
resultArr=[[]for i in range(V)]
for i in range (E):
    a, b = map(int, input().split())
    resultArr[a - 1].append(b - 1)
    resultArr[b - 1].append(a - 1)

visit=[0 for i in range(V)]
cnt=[]
def dfs(start,num):
    num+=1
    if start == (find - 1):
        cnt.append(num)
    visit[start] = 1
    for w in resultArr[start]:
        if visit[w]==0:
            dfs(w,num)
dfs(search-1,0)
if(len(cnt)==0):
    print("-1")
else:
    print(cnt[0]-1)