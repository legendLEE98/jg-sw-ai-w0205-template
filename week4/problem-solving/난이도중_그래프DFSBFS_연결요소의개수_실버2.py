# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724


from collections import deque

userInput = list(map(int, input().split()))

graph = {i:[] for i in range(userInput[0])}
for i in range(userInput[1]):
    inputNode = list(map(int, input().split()))

    graph[inputNode[0] - 1].append(inputNode[1] - 1)
    graph[inputNode[1] - 1].append(inputNode[0] - 1)

block = deque([0])

visited = []
result = 0
# 여기에서 block while문이 종료 될 때 마다 result += 1하면 될듯
while len(visited) != userInput[0]:
    while block:
        curNode = block.popleft()
        for i in range(len(graph[curNode])):
            if graph[curNode][i] not in visited:
                visited.append(graph[curNode][i])
                block.append(graph[curNode][i])
    block.append(len(visited))
    result += 1


print(result)