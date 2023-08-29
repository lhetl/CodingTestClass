R,e=map(int,input().split())
arr=[]
for i in range(e):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda t : t[2])

p=[]
for i in range(R):
    p.append(i)
def find(u):  # find 연산
    if u != p[u]:
        p[u] = find(p[u])  # 경로압축
    return p[u]


def union(u, v):  # union 연산
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1


tree_edges = 0
mst_cost = 0
mst=[]
while True:
    if tree_edges == R - 1:
        break
    u,v, wt = arr.pop(0)  # 다음 최소 가중치 간선 가져오기
    u-=1
    v-=1
    if find(u) != find(v):
        union(u,v)
        mst.append((u,v))  # 트리에 (u, v) 추가
        mst_cost += wt
        tree_edges += 1
print(mst_cost)