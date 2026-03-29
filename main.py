nums = [1,2,3,1]

max1 = 0
max2 = 0

n = len(nums)

if n % 2 == 0:
    for i in range(0, len(nums) // 2):
        max1 += (nums[i * 2])
        max2 += (nums[(i * 2) + 1])
if n % 2 == 1:
    for i in range(0, (len(nums) // 2) + 1):
        max1 += (nums[i * 2])
        max2 += (nums[(i * 2) - 1])

print(max1)
print(max2)