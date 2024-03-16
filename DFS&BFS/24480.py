import sys
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
sorted_graph = [[] for _ in range(n+1)]
visited = [0] * (m+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    sorted_graph[i] = sorted(graph[i], reverse= True)

cnt = 1
def dfs(visited, graph, r): # 정점 집합, 간선 집합, 시작정점
    global cnt
    visited[r] = cnt # visited[이번에 방문하는 정점]에 방문한 순서를 저장
    for i in graph[r]:
        if visited[i] == 0: # 방문하지 않은 경우,
            cnt += 1 # cnt를 증가시킴
            dfs(visited, graph, i)

dfs(visited, sorted_graph, r)

for i in range(1, n+1):
    print(visited[i])
    