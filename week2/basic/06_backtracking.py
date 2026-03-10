"""
[백트랙킹 - 조합 생성]

문제 설명:
- n개의 숫자 중에서 k개를 선택하는 모든 조합을 찾습니다.
- 백트랙킹을 사용하여 가능한 모든 조합을 탐색합니다.
- 조합은 순서가 없으므로 [1,2]와 [2,1]은 같은 조합입니다.

입력:
- n: 전체 숫자의 개수 (1부터 n까지)
- k: 선택할 숫자의 개수

출력:
- 모든 가능한 조합의 리스트

예제:
입력: n = 4, k = 2
출력: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

힌트:
- 백트랙킹의 3단계: 선택(Choose) → 탐색(Explore) → 취소(Unchoose)
- 현재 숫자보다 큰 숫자만 선택하여 중복 방지
"""

def combinations(n, k):
    # 4랑 2를 가정
    """
    1부터 n까지 숫자 중 k개를 선택하는 모든 조합 찾기
    
    Args:
        n: 전체 숫자 개수
        k: 선택할 개수
    
    Returns:
        모든 조합의 리스트
    """
    result = []
    
    def backtrack(start, current_combination):
        """
        백트랙킹 헬퍼 함수
        
        Args:
            start: 탐색을 시작할 숫자
            current_combination: 현재까지 선택한 숫자들
        """
        # 어차피 함수 입력값은 1부터 시작하는거고
        # start에 1 더해서 return 시켜주면 되는거고.
        # 만약 K값과 curCombination의 길이가 같다면면
        if k == len(current_combination):
            result.append(current_combination.copy())
            return result

        # TODO: base case - k개를 모두 선택했으면 결과에 추가
        pass

        # 딱 여기까지가, start 값에 따라서 재시도하는 로직까지 완성 된건데,
        for i in range(start, n+1):
            current_combination.append(i)
            backtrack(i+1, current_combination)
            current_combination.pop()
            # start = 시작 숫자잖아.
            # cur_combi에 담을 숫자 마련해야 하고,
            # start + 1 / 담을 숫자를 인자값으로 해서 재귀 돌리면 됨
            # 마지막으로 넣은 값 하나를 팝해서 새로 대입해야 하니까 pop 갈기고. 

        # 백트랙 지나가면
        #  

        # TODO: start부터 n까지 숫자를 하나씩 시도
        ## TODO: 백트랙킹 3단계 구현
        ## 1. 선택(Choose)
        ## 2. 탐색(Explore)
        ## 3. 취소(Unchoose)
    
    backtrack(1, [])
    return result

def combinations_itertools_compare(n, k):
    """
    itertools를 사용한 조합 생성 (비교용)
    """
    from itertools import combinations as comb
    return [list(c) for c in comb(range(1, n+1), k)]

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 테스트 케이스 1 ===")
    n1, k1 = 4, 2
    result1 = combinations(n1, k1)
    print(f"C({n1}, {k1}) = {result1}")
    print(f"총 {len(result1)}개의 조합")
    print()
    
    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    n2, k2 = 5, 3
    result2 = combinations(n2, k2)
    print(f"C({n2}, {k2}) = {result2}")
    print(f"총 {len(result2)}개의 조합")
    print()
    
    # 테스트 케이스 3
    print("=== 테스트 케이스 3 ===")
    n3, k3 = 3, 1
    result3 = combinations(n3, k3)
    print(f"C({n3}, {k3}) = {result3}")
    print(f"총 {len(result3)}개의 조합")
    print()
    
    # 테스트 케이스 4
    print("=== 테스트 케이스 4 ===")
    n4, k4 = 4, 4
    result4 = combinations(n4, k4)
    print(f"C({n4}, {k4}) = {result4}")
    print(f"총 {len(result4)}개의 조합")

