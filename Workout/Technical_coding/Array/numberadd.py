def incOfNum(Arr):
    res=[]
    nums=""
    for i in Arr:
        nums+=str(i)
    nums=int(nums)+1

    while(nums>0):
        last=nums%10
        res.append(last)
        nums=nums//10
    
    res=res[::-1]
    return res

Arr=[1,2,3]
print(incOfNum(Arr))