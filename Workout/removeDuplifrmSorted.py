# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def rmvDuplifrmSort(arr):
    new=[]
    for elem in arr:
        if elem not in new:
            new.append(elem)

    for j in range(len(res)):
            nums[j] = res[j]

    return len(new)
nums = [1,1,2]
print(rmvDuplifrmSort(nums))

