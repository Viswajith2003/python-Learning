#Find the intersection between two lists

def InterSection(num1,num2):
    res=[]
    for i in range(len(num1)-1):
        for j in range(len(num2)-1):
            if num1[i]==num2[j]:
                res.append(num2[j])
    return res


num1=[1,2,2,5]
num2=[2,2]
ans=InterSection(num1,num2)
print(ans)

