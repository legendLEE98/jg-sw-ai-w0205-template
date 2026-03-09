# 중복된 값 제거하고 순서대로 나열하기.

nums = [1,2,2,3,4,5,6,6] 

# 마지막으로 변경한 위치
# 현재 위치

# 핵심은 nums를 돌아가면서 점검해야 함.
# 0이랑 1을 검사를 함
# 값이 다름.
# 그럼 지나감.
# 만약에 1이랑 2가 숫자가 같음.
# 1이랑 2는 같으니까, 
# 다음에 변경해야할 위치는 2가 되는거임.
# 만약 2랑 3이 달라.
# 그러면 아까 바꿔야 할 위치가 2였으니까
# 해당 값에 index[3] 값을 대입함 
# 이제 그럼 3이랑 4를 비교함.. 반복

last_written = 1
val = 1

for i in range(1, len(nums)):
    if nums[i - 1] != nums[i]:
        nums[last_written] = nums[i]
        val += 1
        last_written += 1

print(val)
print(nums)