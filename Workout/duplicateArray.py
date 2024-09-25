# Input: n = 4, arr[] = [0,3,1,2]
# Output: -1
# Explanation: There is no repeating element in the array. Therefore output is -1.
# Input: n = 5, arr[] = [2,3,1,2,3]
# Output: 2 3 
# Explanation: 2 and 3 occur more than once in the given array.

def duplicate(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)-1):
            if arr[i]==arr[j]:
                dupli=arr[i]
                return dupli
            else:
                return -1
    
arr=[2,3,1,2,3]
print(duplicate(arr))