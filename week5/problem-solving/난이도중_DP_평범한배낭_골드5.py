# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

# 물건 종류 - n
# 준서의 힘 - k
N, K = map(int, input().split())

bag = []
for i in range(N):
    bag.append(list(map(int, input().split())))

# 2차원 리스트 dp
# 준서의 힘만큼,
# 준서의 물건 개수만큼 선언
dp = [[0]*(K+1) for _ in range(N+1)]

# 0은 물건도, 무게도 0개라는 가정이니까 1부터 시행.
for i in range(1,N+1): # 물건의 개수
    for j in range(1,K+1): # 최대 중량
        if j >= bag[i-1][0]:  
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])