# Find the Unique Elements in the Given List without using inbuilt Function
# nums=[1,8,1,2,3,2,4,5,4,5]

def UniqEle(arr):
    uniq=[]
    for ele in arr:
        if ele not in uniq:
            uniq.append(ele)
    return uniq


arr=[1,8,1,2,3,2,4,5,4,5]
print(UniqEle(arr))
