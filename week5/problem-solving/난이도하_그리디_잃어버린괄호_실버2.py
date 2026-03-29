# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

# 풀이 방법
# -가 존재하는 위치까지 input을 전부 더함
# 그 이후 모든 값은 전부 빼기

# 일단 exp 기준으로 모든 배열 자름
exp = input().split('-')

# 정답 값 선언
result = 0

# 첫 배열을 + 기준으로 자름. -시작의 경우는 고려x
# '가장 처음과 마지막 문자는 숫자'
for i in exp[0].split('+'):
    print(exp)
    result += int(i)

for i in exp[1:]:
    print(exp)
    for j in i.split('+'):
        result -= int(j)

print(result)