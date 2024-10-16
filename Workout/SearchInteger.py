#Given a list of integers,search the integer in the given list
# nums=[0,1,2,4,12]
# search=4
# output= 4 found at index 3

def srchInt(nums,srch):
    for i in range(len(nums)):
        if nums[i] == srch:
            return i

nums=[0,1,2,4,12]
srch=int(input("Enter the srch element:"))

index=srchInt(nums,srch)
if index != -1:
    print(f"{srch} found at index {index}")
else:
    print(f"{srch} not found at the list")
