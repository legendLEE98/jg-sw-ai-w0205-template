# 실험 케이스
testCase = int(input())

# 잔돈
change = []
# 동전 종류
coins = [25, 10, 5 ,1]
result = [[] for _ in range(testCase)]

for _ in range(testCase):
    change.append(int(input()))

for i in range(testCase):
    for j in range(len(coins)):
        result[i].append(change[i] // coins[j])
        change[i] = change[i] % coins[j]

for i in range(len(result)):
    print(" ".join(map(str, result[i])))