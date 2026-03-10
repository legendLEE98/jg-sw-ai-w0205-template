inputBoard = []
inputBoard.append(['a', 'b', 'c', 'e'])
inputBoard.append(['s', 'f', 'c', 's'])
inputBoard.append(['a', 'd', 'e', 'e'])


for i in range(len(inputBoard)):
    print(inputBoard[i])



canMove = []
# 사실 상하좌우인건 알 필요가 없음. 인접한 밸류만 있으면 됨.
def checkStr(col:int, row:int) -> list:
    return
# for row in range(len(inputBoard)):
#     for col in range(len(inputBoard[i])):
print(inputBoard[0][-3])


# 받는 값이 현재 위치잖아
# 현위치의 i + 1, -1 리스트업해서 append 하고,