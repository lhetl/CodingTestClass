weights = [(0, 1, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5),
           (1, 6, 3), (2, 3, 9), (2, 4, 7), (2, 5, 2),
           (3, 5, 4), (3, 6, 8), (4, 6, 1), (5, 6, 6)]

weights.sort(key=lambda t: t[2])  # 가중치 기준으로 정렬
print(weights)
mst = []
N = 7  # 그래프 정점 수
p = []
for i in range(N):  # 각 정점 자신이 집합의 대표(루트)
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
while True:
    if tree_edges == N - 1:
        break
    u, v, wt = weights.pop(0)  # 다음 최소 가중치 간선 가져오기
    if find(u) != find(v):
        union(u, v)
    mst.append((u, v))  # 트리에 (u, v) 추가
    mst_cost += wt
    tree_edges += 1
print('최소신장트리: ', end='')
print(mst)
print('최소신장트리 가중치:', mst_cost)