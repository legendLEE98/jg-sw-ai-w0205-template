# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

money = list(map(int, input().split()))

coins = []
for i in range(money[0]):
    coins.append(int(input()))

result = 0
for i in range(len(coins) - 1, -1, -1):
    result += money[1] // coins[i]
    money[1] = money[1] % coins[i]

print(result)

# for i in range(len(coins)):