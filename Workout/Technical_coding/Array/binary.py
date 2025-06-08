def binarytodec(nums):
    nums=str(nums)
    res=0
    length=len(nums)
    for i in range(length):
        digit=int(nums[i])
        power=2**(length-i-1)
        res+=digit*power
    return res

nums=1101
print(binarytodec(nums))