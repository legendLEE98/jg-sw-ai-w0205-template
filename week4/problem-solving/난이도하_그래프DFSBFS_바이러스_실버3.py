# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606


from collections import deque
# 일단 input부터

node = int(input())
line = int(input())

graph = [[] for _ in range(node + 1)]
for i in range(1, line + 1):
    a, b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a]

# 그래프는 얻었고
# 시작지는 1 부터 해야함.
# 설계 방식
# 1. 비감염PC vector
# 2. 감염됐는지 파악하는 inpected

def computer_virus(graph, start):
    vector = deque([start])

    infected = []
    infected.append(start)

    while vector:
        curPC = vector.popleft()
        for close in graph[curPC]:
            if close not in infected:
                vector.append(close)
                infected.append(close)

    return len(infected)

print(computer_virus(graph, 1) - 1)