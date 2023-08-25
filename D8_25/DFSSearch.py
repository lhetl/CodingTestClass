adj_list =[[1,3,5],[0,2,3],[1,4], [0,1,4,5],[2,3],[0,3],[7],[6] ]
N = len(adj_list)
visited = [None] * N


def dfs(v):
 visited[v] = True
 print(v, end=' ')
 for w in adj_list[v]:
  if not visited[w]:
   dfs(w)
print('DFS 방문 순서:')
for i in range(N):
 if not visited[i]:
  dfs(i)