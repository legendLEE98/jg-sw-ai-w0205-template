# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

# 전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.

# 전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 
# <그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 

# 나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은 색으로 칠해져 있지 않으면 
# 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 
# 이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 
# 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.

# 위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1>의 종이를 처음 나눈 후의 상태를, 
# <그림 4>는 두 번째 나눈 후의 상태를, <그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와 
# 7장의 파란색 색종이를 보여주고 있다.

# 일단 x랑 y좌표를 받아야 함

size = int(input())
paper = [[0 for col in range(size)] for row in range(size)]

for i in range(size):
    paper[i] = list(map(int, input().split()))

blueBox = 0
whiteBox = 0
# 분류 체크 
def check(paramPaper, leftX, rightX, leftY, rightY)-> bool:
    # 전부 흰색일 경우, 전부 파란색일 경우 True
    # 여기서 카운팅해보기 일단
    countB = 0
    countW = 0

    for y in range(leftY, rightY):
        for x in range(leftX, rightX):
            if paramPaper[y][x]:
                countB += 1
            else:
                countW += 1

            if countB > 0 and countW > 0:
                return False
    return True

# 여기서도 매개변수를 받되,
# 하나만 조사해서 그게 흰색이면 whiteBox += 아니면 BlueBox 올리자
def add(paramPaper, leftX, leftY):
    global blueBox, whiteBox
    if paramPaper[leftY][leftX]:
        # 이 조건은 1일 경우니까
        blueBox += 1
    else:
        whiteBox += 1

def spliter(paramPaper, leftX, rightX, leftY, rightY):
    # 일단 mid 먼저 구하기
    midX = (leftX + rightX) // 2
    midY = (leftY + rightY) // 2


    # 사분면으로 분해해서 테스트
    # 우선 전체적으로 먼저 확인
    if check(paramPaper, leftX, rightX, leftY, rightY):
        add(paramPaper, leftX, leftY)
        return
    
    # 좌상
    if check(paramPaper, leftX, midX, leftY, midY):
        add(paramPaper, leftX, leftY)
    else:
        spliter(paramPaper, leftX, midX, leftY, midY)


    # 우상
    if check(paramPaper, midX, rightX, leftY, midY):
        add(paramPaper, midX, leftY)
    else:
        spliter(paramPaper, midX, rightX, leftY, midY)
    

    # 좌하
    if check(paramPaper, leftX, midX, midY, rightY):
        add(paramPaper, leftX, midY)
    else:
        spliter(paramPaper, leftX, midX, midY, rightY)


    # 우하 
    if check(paramPaper, midX, rightX, midY, rightY):
        add(paramPaper, midX, midY)
    else:
        spliter(paramPaper, midX, rightX, midY, rightY)

# def spliter(paramPaper, leftX, rightX, leftY, rightY):

spliter(paper, 0, size, 0, size)

print("흰 영역 : ", whiteBox , '\n', "파란 영역 : ", blueBox)