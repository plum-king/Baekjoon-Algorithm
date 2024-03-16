import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def bfs(visited, graph, r):
    q = deque([r])
    visited[r] = 1
    cnt = 2
    
    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = cnt
                cnt += 1
            
bfs(visited, graph, r)

for i in range(1, n+1):
    print(visited[i])