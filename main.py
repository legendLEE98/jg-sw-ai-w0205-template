def find_duplicates_hash(nums):
    """
    방법3: 해시 집합 사용
    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    seen = set()
    duplicates = set()
    # 돌면서 set에 추가
    # set 추가 == add
    for i in range(len(nums)):
        if nums[i] in seen:
            duplicates.add(nums[i])
        else:
            seen.add(nums[i])

    # TODO: 각 원소를 순회하면서
    ## 이미 seen에 있으면 duplicates에 추가
    ## 없으면 seen에 추가
    
    return list(duplicates)


value = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates_hash(value))