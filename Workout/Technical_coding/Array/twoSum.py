def twoSum(Arr,Target):
    for i in range(len(Arr)):
        for j in range(i+1,len(Arr)):
            if Arr[i]+Arr[j]==Target:
                return i,j


Arr=[2,7,11,15]
Target=9
print(twoSum(Arr,Target))