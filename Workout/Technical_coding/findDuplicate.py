# Input: n = 4, arr[] = [0,3,1,2]
# Output: -1
# Explanation: There is no repeating element in the array. Therefore output is -1.
# Input: n = 5, arr[] = [2,3,1,2,3]
# Output: 2 3 
# Explanation: 2 and 3 occur more than once in the given array.


# n=int(input("Enter the element:"))
def findDupli(arr):
    dupli=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                dupli.append(arr[i])
    if not dupli:
        return -1
    else:
        return dupli
        
            
arr=[2,3,1,3,4,2]
print(findDupli(arr))




















