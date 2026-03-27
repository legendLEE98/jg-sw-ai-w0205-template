# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904


n = int(input())

dp = [0] * (n + 2)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
    pass

print(dp[n])