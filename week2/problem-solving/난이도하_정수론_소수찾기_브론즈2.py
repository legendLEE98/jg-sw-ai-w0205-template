import math
# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

# 문제 조건
# input을 두 번 받음
# 처음엔 숫자
# 두 번째엔 슬라이스 해야할 숫자 나열 
# ex)
# 5
# 1 3 4 7 9

# 소수는 어떻게 구할까?
# 입력받은 수를 제곱했을 때 나온 값만큼
# ex) 루트10 => 3.16이니까
# 1, 2, 3으로 나눠볼 수 있음.
# 1, 2, 3은 이제 나눗셈을 시도해볼 수 있는 숫자인데
# 만약에 저 셋 중에 1을 제외하고 나머지가 없는 숫자로 나눌 수 있다면?
# 그건 소수가 아닌거임

# 즉 플래그 관리를 해서, 루트씌운값을 테스트해보면 정확한 값을 얻을 수 있다~ 가 됨.


# for i in range(2, 3):
#     print(i)


# a = 11 # 퍼스트 밸류에 해당 됨
a = int(input())

# b = "0 1 2 3 4 5 6 7 8 9 10" # 세컨드 밸류에 해당 됨
b = input()

b = b.split()
# 이제 값은 받았음.
# 받은 값들을 하나하나씩 루트를 씌워봐야 함. 몇 번? a번만큼.

sosu = 0

# c의 첫 번째 인자값부터 하나씩.
for i in range(a):
    flag = False

    b[i] = int(b[i])
    if b[i] <= 1:
        continue

    # int형변환 했으니까 이거 루트 씌워봐야 함.
    rootVal = math.sqrt(b[i])
    # 정수형 형변환
    rootVal = int(rootVal)
    
    # 만약에 여기서 루트씌웠는데 1이하인 경우는 지금 2, 3밖에 없음
    # 그렇다면 여기에서 1인 경우는 2나 3인데 이 둘은 소수가 맞으니까 소수 라는 값을 하나 증가시키면 됨.
    if rootVal <= 1:
        print(b[i])
        sosu += 1
        continue
    
    for j in range(2, rootVal + 1): #2와 rootVal이 값이 같으면 실행 자체가 안돼서 추가함.
        if b[i] % j == 0:
            # 이걸 했을 때 0이 나오는 경우는 flag를 true로 만들어
            flag = True

        if flag == True:
            break

            
    if flag == False:
        print(b[i])
        sosu += 1
            
print(sosu)