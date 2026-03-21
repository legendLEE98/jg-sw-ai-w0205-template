# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

stage = int(input())
coordinate = [[] for _ in range(stage)]
for i in range(stage):
    coordinate[i] = list(map(int, input().split()))
# 좌표니까 그냥 일단 x, y축으로 해봅시다.

def dfs(coordinater, curX, curY, visited = None):
    if visited == None:
        visited = set()

    if curY >= stage or curX >= stage:
        return "Hing"
    if (curX, curY) in visited:
        return "Hing"
    
    
    if coordinater[curY][curX] == -1:
        return "HaruHaru"
    visited.add((curX, curY))

    value = coordinater[curY][curX]
    # 오른쪽으로 가는 조건
    # curX + coordinate(curx, cury)
    result = dfs(coordinater, curX + value, curY, visited)
    if result == "HaruHaru":
        return "HaruHaru"
    result = dfs(coordinater, curX, curY + value, visited)
    if result == "HaruHaru":
        return "HaruHaru"
    
    return "Hing"

print(dfs(coordinate, 0, 0))