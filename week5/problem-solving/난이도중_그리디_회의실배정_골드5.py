# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

order = int(input())

reserv = []
for i in range(order):
    reserv.append(list(map(int, input().split())))

reserv.sort(key=lambda x: x[1])

result = 0
time = 0
for start, end in reserv:
    if start >= time:
        time = end
        result += 1
print(result)