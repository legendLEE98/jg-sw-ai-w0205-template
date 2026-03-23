# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

# 다시 풀어봐야 할듯

# 노드 개수
nodeNums = int(input())

# 작업 개수
graph = {i:[] for i in range(nodeNums)}
duration = [0] * (nodeNums)
result = [0] * (nodeNums)

for i in range(0, nodeNums):
    inputData = list(map(int, input().split()))
    duration[i] = inputData[0]
    graph[i] = [val - 1 for val in inputData[2:]]


# i번째 값의 선행 조건을 먼저 찾기

for i in range(nodeNums):
    if graph[i] == []:
        result[i] = duration[i]
    result[i] = max(result[j] for j in graph[i]) + duration[i]

print(max(result))