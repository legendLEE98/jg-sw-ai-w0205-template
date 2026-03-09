import math
# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020


# 문제
# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 
# 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 
# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 
# 이러한 수를 골드바흐 수라고 한다. 
# 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 
# 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

# 1. 받은 밸류의 모든 소수를 찾는 알고리즘이 필요함 - 완료
# 문제 다시 읽자
# 2보다 큰 모든 짝수는 소수의 합계로 나타낼 수 있다.
# 그러면 1만까지의 소수를 먼저 구해야겠네.

# 2. 밸류를 [i] 순서로 빼서, 남은 밸류가 소수인지 판별하는 알고리즘도 필요함
# 2-1. 밸류를 [n, m]으로 보관하는 2차원 배열이 필요함
# 3. 최종적으로 n,m 중 n-m 혹은 m-n이 가장 낮은 수를 찾아야 함.

counting = int(input())
inputValue = []
primeList = []
candidate = []

# inputValue는 primeList의 특정 위치의 값이 들어갈 예정
# 즉, primeList[i]가 될 예정
# 이제 이 수가 소수인지 판단. 2부터 해야함.
def findPrime(prime):
    for i in range(2, prime):
        flag = False

        # i가 2 혹은 3일 경우 primeList.append(i)을 추가함. 
        if i == 2 or i == 3:
            primeList.append(i)
            continue
        
        result = root(i)

        # 이미 if에서 2랑 3을 걸러오기 때문에 상관없음.
        for j in range(2, result + 1):
            if i % j == 0:
                flag = True
                
        if flag == False:
            primeList.append(i)

def root(value):
    result = math.sqrt(value)
    return int(result)


for i in range(0, counting):
    inputValue.append(int(input()))

def bigValue():
    curVal = 0
    for i in range(0, len(inputValue)):
        if curVal < inputValue[i]:
            curVal = inputValue[i]
    findPrime(curVal)

bigValue()
print(primeList)
print(inputValue)

# 이제 여기서 값 찾기
def result():
    for i in range(0, counting):
        

# 값 찾기 반복 횟수는 카운팅 횟수로 해야함.
# 소수 리스트(primeList) 받았고, 입력값 리스트(inputValue)도 받았음.


# 모든 소수 찾기로 문제를 꺾어야함
# findPrime으로 이름 바꾸고,
# 항상 실행되게 먼저 해야함.

# print(root(inputValue[0]))
    # 소수 어케찾지 => 나누기