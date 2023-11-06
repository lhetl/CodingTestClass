maxP,n=map(int,input().split())
kp=[]
tmp=list(map(int,input().split()))
kp=tmp[1:]
pl=[[] for i in range (n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    pl[i]=tmp[1:]
if(len(kp)==0):
    print(n)
    exit(0)
ans=0
#파티 참여하는 사람 그래프를 만들어 한번 kp일경우 그 사람과 연결된 모든 사람 kp로 해야함
arr=[[] for i in range(maxP+1)]
for i in pl:
    if len(i)<2:
        continue
    for j in i:
        for k in i:
            if k not in arr[j]:
                arr[j].append(k)
        if j in arr[j-1]:
            arr[j-1].remove(j)
# print(arr,kp)
visited=[False]*len(arr)
def dfs(v):
    visited[v] = True
    if v not in kp:
        kp.append(v)
    for i in arr:
        if v in i:
            for w in i:
                if not visited[w]:
                    dfs(w)
for i in kp:
    dfs(i)
for i in pl:
    check=True
    for j in i:
        if visited[j]==True:
            check=False
            break
    if check:
        ans+=1
print(ans)