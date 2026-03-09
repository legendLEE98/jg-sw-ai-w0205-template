# 핵심. 아주 기초적인 것 부터 함수로 선언해서 타고타고 올라간다.
# 반대로, 고차원에서 필요한걸 하나씩 만들어서 점점 디테일한 부분으로 내려간다.

# applicate order
# normal order evalution



# Iteration
def nsum(n):
    result = 0
    for i in range(0, n+1):
        result += i

# Recursion
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
    

print(sum(10))

# 베이스컨디션 << 중요
# 근데 이러면 중간값 추적이 안됨.


# tail recursion
def sum_iter(n, total):
    if n == 0:
        return total
    return # TODO

# 파라미터 하나 더 받았을 뿐인데.
# 본인만 부르는 방법으로 바뀌었음.

def expt_iter(n,m,product):
    return 1

def expt(n,m):
    return 1

def exp(n):
    if n == 0:
        return 1
    return n * exp()

# 뭔 함수가 실행됐는지 추적할 수 있는 방법? 이게 필요할듯

# 전체를 제곱하면 제곱수*2가 됨.
def FE(n,m):
    if n == 0:
        return 1

def FEH(n,m):
    return 1    

# 피보나치 수열
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(1) + fib(n-2)
# 여기부터 연산이 매우 많이 들어감.

# 이걸 tail - recursion으로 만들면 불필요한 연산이 더 줄어듦


