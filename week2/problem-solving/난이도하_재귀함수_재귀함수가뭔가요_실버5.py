# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

totalCount = int(input())

word = []
word.append('"재귀함수가 뭔가요?"')
word.append('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
word.append('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
word.append('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

word.append('"재귀함수는 자기 자신을 호출하는 함수라네"')
word.append("라고 답변하였지.")

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

# retryCount는 반복 횟수

# 토탈 카운트가 3으로 되면
# 3번 반복을 해야하는데.
# retryCount는 언제 더함? 호출할 때.


# 일단 토탈 카운트가 들어가야 하는건 맞음.
# 토탈 카운트를 감소시키는 방향으로 해야할듯?
def reFunction(inputValue):
    # 재귀함수가 뭔가요는 항상 들어감.
    print("____" * (totalCount - inputValue), end='')
    print(word[0])

    if inputValue == 0:
        print("____" * (totalCount - inputValue), end='')
        print(word[4])
        print("____" * (totalCount - inputValue), end='')
        return print(word[5])
    
    else:
        # 그 외의 경우에는 일단 멘트 출력하고,
        # 리트라이 카운트 증가시켜서 재호출 시켜야 함.
        # 그 이후 라고 답변하였지 출력해야 함.
        for i in range(1,4):
            print("____" * (totalCount - inputValue), end = '')
            print(word[i])
        # 위에 호출 끝나면 현재 함수 다시 호출해야 함.
        reFunction(inputValue - 1)

        print("____" * (totalCount - inputValue), end = '') # 여기에서 현재 curCount의 갯수만큼 '____' 추가
        return print(word[5])

reFunction(totalCount)

# 어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
# "재귀함수가 뭔가요?"
# "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# 그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ____"재귀함수가 뭔가요?"
# ____"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# ____마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# ____그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ________"재귀함수가 뭔가요?"
# ________"재귀함수는 자기 자신을 호출하는 함수라네"
# ________라고 답변하였지.
# ____라고 답변하였지.
# 라고 답변하였지