
def pairsFind(Arr,Target):
    Arr.sort()
    l=0
    r=len(Arr)-1
    while(l<=r):
        if Arr[l]+Arr[r]<Target:
            l=l+1
        elif Arr[l]+Arr[r]>Target:
            r=r-1
        elif Arr[l]+Arr[r]==Target:
            print("The values are",Arr[l],"&",Arr[r])
            r=r-1
            l=l+1
    return None
    
Arr=[5,7,4,3,9,8,19,21]
Target=17
pairsFind(Arr,Target)    
    

