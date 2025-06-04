nums = [5, 4, -1, 7, 8]
n = len(nums)
res = nums[0]
cur = nums[0]
for i in range(1, n):
    cur = max(nums[i], nums[i] + cur)
    res = max(res, cur)
print(res)
