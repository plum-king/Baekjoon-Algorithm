# 문제 이해
# 시작 정점에서부터 방문하는 정점의 순서를 표기하되, i번째 줄에는 정점 i의 방문 순서를 출력하기 때문에
# 예를 들어 정점 2번은 2번째 줄에 몇 번째 순서로 방문되었는지 작성하면 된다.

# sorted(정렬할 리스트, key = lambda x: 비교할 연산자 한 개인 경우)
# sorted(정렬할 리스트, key = lambda x: (비교할 연산자 여러 개인 경우))

import sys
sys.setrecursionlimit(10 ** 6)
# 파이썬의 기본 재귀 깊이 제한: 1000
# 재귀로 문제를 풀 경우, 이 제한에 걸릴 확률 높음

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)] # 0번째는 사용하지 않으므로 정점 개수보다 한 개 더 많게
visited = [0] * (n+1) # 위와 동일한 이유로 한 개 더 많게 설정

cnt = 1
def dfs(graph, r, visited):
    global cnt
    visited[r] = cnt # 방문 시 cnt 증가
    for i in graph[r]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)
    return

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    # 입력 받은 그래프를 아래 형태 변환

    # graph = 
    # [
	#   [],
    #   [4, 2], 
    #   [1, 3, 4],
	#   [2, 4],
    #   [1, 2, 3],
    #   [],
    # ]
    
for i in range(n+1):
    graph[i].sort()
# sorted_graph = sorted(graph, key = lambda x: (x[0], x[1])) 

dfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])