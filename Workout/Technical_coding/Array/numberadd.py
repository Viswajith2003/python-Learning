def incOfNum(Arr):
    res=[]
    nums=""
    for i in Arr:
        nums+=str(i)      #123
    nums=int(nums)+1      #124    

    while(nums>0):    
        last=nums%10
        res.append(last)
        nums=nums//10     #res=[4,2,1]
    
    res=res[::-1]         #res=[1,2,4]  
    return res

Arr=[1,2,3]
print(incOfNum(Arr))