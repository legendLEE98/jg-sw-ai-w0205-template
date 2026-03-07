import copy
"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

힌트:
- 회전 후 위치: (i, j) -> (j, n-1-i)
- 새로운 배열을 만들어 값을 채워넣으세요
"""


# 무조건 가로로 진행됨

# 다시 돌아와서 i, j -> j, n-1-i 가 된다는 건데
# 그럼 먼저 해야할 건 순서를 바꾼다는 것.
# 로테이트 기능은 모든 변수에 한 번씩 해주면 되잖아.
# 배열을 활용한다는게 즉
# 1차원 배열과 2차원 배열의 순서를 바꾸고
# [2][1] -> [1][2]
# 다음에 하는건 3 - 1 - i인데, i는 2니까
# [1][0]이 된다. 검증해볼까 헐 맞음
# 이거 값을 옮기는건가?
# 구현 방법이 그러니까..


a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
b = a

a = 3

print(b)

# matrix = [1,2,3]
# #     [4,5,6],
# #     [7,8,9]
# # ]
# copied_list = copy.deepcopy(matrix)

# # 내가 해야할 것 => 깊은 복사


# def rotate(matrix):
#     length = len(matrix)
#     manuscripts = copy.deepcopy(matrix)

#     for num in enumerate(range(length)):
#         print(num)
#         # for j in range(length):
#         #     print(i, j)
#         #     change = length - 1 - i
#         #     matrix[j][change] = copy.deepcopy(manuscripts[j][change])

# rotate(matrix)

# print(matrix)
            
# def print_matrix(matrix):

#     for row in matrix:
#         print(row)

# print_matrix(matrix)
        

# def print_matrix(matrix):
#     """배열을 보기 좋게 출력하는 헬퍼 함수"""
#     for row in matrix:
#         print(row)

# print_matrix(matrix)





# def rotate_matrix_90(matrix):
#     """
#     2차원 배열을 시계방향으로 90도 회전
    
#     Args:
#         matrix: N x N 2차원 리스트
    
#     Returns:
#         회전된 2차원 리스트
#     """
#     n = len(matrix)

#     print(n)
    
#     # TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화)
#     for col in range(n):
#         for row in range(n):
#             matrix[col][row] = 0

#     pass
        
#     # TODO: 원본 배열의 각 요소를 회전된 위치에 배치하세요
#     # 힌트: (i, j) 위치의 요소는 회전 후 (j, n-1-i) 위치로 이동

#     # 각 배열을 회전시킨다는건, 각 요소의 위치를 바꾼다는 것.


#     rotated = n
#     pass
    
#     return rotated

# def print_matrix(matrix):
#     """배열을 보기 좋게 출력하는 헬퍼 함수"""
#     for row in matrix:
#         print(row)

# # 테스트 케이스
# if __name__ == "__main__":
#     # 테스트 케이스 1: 3x3 배열
#     matrix1 = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
    
#     print("원본 배열:")
#     print_matrix(matrix1)
#     print("\n회전 후:")
#     rotated1 = rotate_matrix_90(matrix1)
#     print_matrix(rotated1)
#     print()
    
#     # 테스트 케이스 2: 4x4 배열
#     matrix2 = [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16]
#     ]
    
#     print("원본 배열:")
#     print_matrix(matrix2)
#     print("\n회전 후:")
#     rotated2 = rotate_matrix_90(matrix2)
#     print_matrix(rotated2)


