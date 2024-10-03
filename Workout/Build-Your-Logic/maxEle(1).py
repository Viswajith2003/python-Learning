def Maxele(arr):
    # for i in range(len(arr)):
    #     for j in range(i+1,len(arr)):
    #         if arr[i]<=arr[j]:
    #             return arr[j]
    max=0
    for i in arr:
        if i>=max:
            max=i
    return max



arr=[5,2,6,1,4,3]
print(Maxele(arr))
