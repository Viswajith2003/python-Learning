#Given a list of integers,search the integer in the given list
# nums=[0,1,2,4,12]
# search=4
# output= 4 found at index 3


def srchElem(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return i
        


arr=[0,1,2,4,6]
n=int(input("Enter the searching element:"))
index=srchElem(arr,n)
if index != -1:
    print(f"{n} is found at index {index}");
else:
    print("element not found")





































# def srchInt(nums,srch):
#     for i in range(len(nums)):
#         if nums[i] == srch:
#             return i

# nums=[0,1,2,4,12]
# srch=int(input("Enter the srch element:"))

# index=srchInt(nums,srch)
# if index != -1:
#     print(f"{srch} found at index {index}")
# else:
#     print(f"{srch} not found at the list")
