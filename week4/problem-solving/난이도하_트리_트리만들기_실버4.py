# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

# n과 m이 주어졌을 때, n개의 노드로 이루어져 있고, 
# m개의 리프로 이루어져 있는 트리를 만드는 프로그램을 작성하시오.

# 항상 정답이 존재하는 경우만 입력으로 주어진다.
# 트리는 사이클이 없는 연결 그래프이고, 리프는 차수가 1인 노드를 의미한다.

# 예제1
# 4 2

# 출력값
# 0 1
# 1 2
# 2 3

tree = int(input())
leaf = int(input())

# 트리의 마지막은 tree - leaf + 1에 해당함
# 만약 4 / 2일 경우 3이 마지막,
# 만약 4 / 3일 경우, 2 / 3이 마지막 노드, (1노드에서 2개 연결)
# 5 / 3일 경우 3 / 4가 마지막 레벨의 노드가 됨. (2 노드에서 2개 연결)

last_parent = tree - leaf
for i in range(0, last_parent):
    print(i, i + 1)

for i in range(last_parent + 1, tree):
    print(last_parent, i)