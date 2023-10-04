import sys
T=int(input())
N,L=map(int,input().split())
g = [[(0,0) for i in range(N)] for i in range(N)]
print(g)
tmp=list(map(int,input().split()))
for i in range(L):
    a,b=map(int,input().split())
    a-=1
    b-=1
    g[a][b]=(b,tmp[a])
last=int(input())
print(g)



s=0
visited = [False] * N  # 초기화
D = [sys.maxsize] * N  # D[i]를 최댓값으로 초기화
D[s] = 0
previous = [None] * N  # 경로를 추출하기 위해
previous[s] = tmp[s]
for k in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):  # 방문 안 된 정점들의 D 원소 중에서 최솟값을 가진 정점 m 찾기
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    visited[m] = True
    for w, wt in g[m]:  # m에 인접한 방문 안 된 각 정점의 D의 원소 갱신
        if not visited[w]:
            if D[m] + wt < D[w]:
                D[w] = D[m] + wt  # 간선 완화
                previous[w] = m
print('정점 ', s, '(으)로부터 최단 거리:')

for i in range(N):
    if D[i] == sys.maxsize:
        print(s, '와(과) ', i, ' 사이에 경로 없음.')
    else:
        print('[%d, %d]' % (s, i), '=', D[i])

print('\n정점 ', s, '(으)로부터의 최단 경로')
for i in range(N):
    back = i
    print(back, end='')
    while back != s:
        print(' <-', previous[back], end='')
        back = previous[back]
    print()