dulpiArr=[1,3,2,3,4,5,6,4,1,2]

def removeDupli(arr):
    new=[]
    for i in arr:
        if i not in new:
            new.append(i)
    return new


print(removeDupli(dulpiArr))