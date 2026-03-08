# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다. 
# 정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.

# 우선 반복할 인풋값을 먼저 받아야함
# 엣지케이스 - '각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림'
# 엣지케이스2 - 이상 이 아니라, 초과 (< / >)

# 첫 인자값은 반드시 학생 수, 두 번째 인자값부터 점수

theClass = int(input())
studentAndScore = []
studentAvg = 0
result = []

for i in range(0, theClass):
    classSum = 0
    scoreList = []
    overAvg = 0

    studentAndScore.append(input())
    studentAndScore[i] = studentAndScore[i].split()

    studentCount = int(studentAndScore[i][0])

    for j in range(1, studentCount + 1):
        scoreList.append(int(studentAndScore[i][j]))
        classSum = classSum + int(studentAndScore[i][j])

    studentAvg = classSum / studentCount

    for j in range(0, len(scoreList)):
        if studentAvg < scoreList[j]:
            overAvg += 1

    result.append(overAvg / studentCount * 100)
    
for i in range(0, i):
    print("{:.3f}".format(result[i]), "%", sep='')

    # 평균 얻었음.
    # 이제 이 평균값을 통해서 평균값 이상인 학생을 찾아야 함.
        

    # if studentCount == j + 1:
    #     studentAvg[i] = classSum / studentCount