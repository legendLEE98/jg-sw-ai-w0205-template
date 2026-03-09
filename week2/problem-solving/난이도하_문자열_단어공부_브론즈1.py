# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157


# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 

# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 문제풀이
# 이거 딕셔너리 쓰면 편할거같은데
# 일단 받은 영단어를 소문자로 치환하고

inputWord = input().lower()

# 이번엔 inputWord의 단어를 리스트에 등록하는 로직 시행
result = {}

for i in range(0, len(inputWord)):
    if inputWord[i] in result:
        result[inputWord[i]] += 1
        continue

    result[inputWord[i]] = 1
    
    #     result[inputWord[i]] += 1
sorted_desc = sorted(result.items(), key=lambda x: x[1], reverse=True)

if len(sorted_desc) == 1:
    print(sorted_desc[0][0].upper())
elif sorted_desc[0][1] == sorted_desc[1][1]:
    print("?")
else:
    print(sorted_desc[0][0].upper())