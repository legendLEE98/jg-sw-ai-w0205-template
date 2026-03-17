# 출력 예시
# [1, 2, 3, 4]


# 분할정복 ->
# 배열을 반으로 쪼갬
# 순서 정렬

# 1. 쪼갬
# HOW? - left + right // 2

# 2. 계속 쪼갬

head = [4,2,1,3]

def sort(arr, left, right):
    if left >= right:
        return
    
    mid = left + right // 2

    print(left, right, mid)

    if left < right:
        sort(arr, left, mid+1)
        sort(arr, mid+1, right)
        merge(arr, left, mid+1, right)
    pass

def merge(arr, left, mid, right):

    # 합쳐야 함.
    # 왼쪽 오른쪽 비교해서,
    # 좀 더 큰 애를 먼저 붙이기
    i = left
    j = mid
    k = left

    # 반복문
    while i < mid and j < right:
        if arr[i] < arr[j]:
            arr[k] = arr[i]
            i += 1
        if arr[j] < arr[i]:
            arr[k] = arr[j]
            j += 1
        k += 1

    if i < mid:
        arr[k] = arr[i]
        i += 1
        k += 1
    if j < right:
        j += 1
        k += 1


print(sort(head, 0, 3))