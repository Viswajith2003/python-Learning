def leaders(n):
    result=[]
    max=n[len(n)-1]
    result.append(max)
    for i in range(len(n)-1,0,-1):
        if n[i]<=n[i-1] and max<=n[i-1]:
            max=n[i-1]
            result.append(max)
    return result

arr=[6,17,8,4,3,5,2]
print(leaders(arr))























# def leaders(arr):
#     result = []
#     max=arr[len(arr)-1]
#     result.append(max)
#     for i in range(len(arr)-1,0,-1):
#         if arr[i]<=arr[i-1] and max<=arr[i-1]:
#             max=arr[i-1]
#             result.append(max)
#     return result

# arr=[6,17,8,4,3,5,2]
# print(leaders(arr))





