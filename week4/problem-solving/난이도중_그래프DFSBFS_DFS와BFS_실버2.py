# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

# dfs로 탐색한 결과
# bfs로 탐색한 결과 출력

# 초기화 먼저
from collections import deque

nodeCount, lineCount, start = map(int, input().split())

graph = {i:[] for i in range(1, nodeCount + 1)}

for _ in range(lineCount):
    node, edge = map(int, input().split())
    
    graph[node].append(edge)
    graph[edge].append(node)

for key in graph:
    graph[key].sort()

# dfs가 쉬우니까 이거 먼저 구현
def dfs(param_graph, param_start, visited = None):
    if visited == None:
        visited = []

    if param_start in visited:
        return

    visited.append(param_start)
    for neighbor in param_graph[param_start]:
        dfs(param_graph, neighbor, visited)


    result = " ".join(map(str, visited))

    return result


def bfs(param_graph, param_start):
    visited = []
    # !!!핵심!!!
    startNode = deque([param_start])
    visited.append(param_start)

    # 스타트 노드가 들어있을 때만 반복
    while startNode:
        curNode = startNode.popleft()
        # 현재 잡고 있는 노드 중, 연결돼있는 모든 노드 탐색
        for neighbor in param_graph[curNode]:
            # 인근값이 방문하지 않은 값이라면
            if neighbor not in visited:
                visited.append(neighbor)
                startNode.append(neighbor)

    result = " ".join(map(str, visited))

    return result


print(dfs(graph, start))
print(bfs(graph, start))