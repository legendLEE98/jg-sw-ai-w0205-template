# chr로 아스키코드를 str 형태로 변환.


# print(chr(97))

# word = []

# for i in (2, 10):

#     for k in (97, 123):
#         word.append(k)

# 매핑에는 2~9가 들어올테니까

mappingList = {}

for i in range(0, 8):
    phoneNum = i + 2

    mappingList[phoneNum] = []

    if i == 5:
        for j in range(0,4):
            mappingList[phoneNum].append(chr(97 + i * 3 + j))
    elif i == 6:
        for j in range(0,3):
            mappingList[phoneNum].append(chr(97 + i * 3 + j + 1))
    elif i == 7:
        for j in range(0,4):
            mappingList[phoneNum].append(chr(97 + i * 3 + j + 1))
    else:
        for j in range(0,3):
            mappingList[phoneNum].append(chr(97 + i * 3 + j))


# 구체적으로 뭘 받는지 생각할 것

# 유저는 2, 3 밖에 입력 안함.
# 2를 메인으로 보낸다면
# 2[0]인 a부터 돌아야 함.



digit = input()
result = []

# 어떤 시점에 리턴해야할까?
# 더 이상 추출할 단어가 없을 때 아닌가?
# 오케이 워드로 받아보자 일단
def recursion(digit, data):
    if digit == "":
        return result.append(data)
    # 종료 되는 조건은 찾았음.

    # 이제 word를 받았으니, word를 추가하는 로직을 만들어야 함
    # 몇 번? word에 매핑된 글자 개수만큼.
    # 그럼 일단 트라이 카운트를 구해야겠네.
    # mappingList[]의 배열 안에 값을 넣어야 하는데.
    # 맨 앞 값만 생각하자.

    # data를 더 받기로 했음. 얘는 str형태인데,
    # 이거를 최종적으로 추가하는거고,
    # 평소에 data에 +로 값을 전달해줘야 해.
    
    # data 관리는 어디서 해야 하는데?

    # 밑에는 그냥 단순하게 0, 3이라고 생각
    for i in range(0, len(mappingList[int(digit[0])])):
        # 그럼 여기에서 반복으로 호출하면 되는건가?
        # a의 워드가 끝날 때 까지 digit[1]에 있는 값을 반복시키면 되겠네?
        recursion(digit[1:], data + mappingList[int(digit[0])][i])
    
print(digit[0])
# data는 스트링형태일거고
# mappingList는 어떻게 가져오지?

# breakpoint()

recursion(digit, "")
print(result)