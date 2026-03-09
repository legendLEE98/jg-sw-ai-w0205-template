# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

# abc -> 이걸 R번 반복
# 2
# aabbcc -> 출력물



# 풀이과정
# 일단 값을 두 번 받아야 함.

total = int(input())
result = []

# result.append("테스트")
# print(type(result[0]))

for k in range(0, total):
    originWord = str(input())
    sliceWord = originWord.split()

    result.append("")

    # 워드를 잘라서 리스트로 보관하고
    # 그 리스트 출력만 하면 될 거 같은데?

    for i in range(0, len(sliceWord[1])):
        # 일단 단어를 가져올 for문 생성
        # 이제 여기서 단어를 쪼개서 넣자
        for j in range(0, int(sliceWord[0])):
            result[k] = result[k] + sliceWord[1][i]

for i in range(0, len(result)):
    print(result[i])

# sliceWord 1은 단어 - 워드
# sliceWord 0은 단어를 반복할 횟수