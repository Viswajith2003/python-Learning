
def common_ele_list(l1,l2):
    # res=[]
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                return l1[i]
            

l1=[40,50,60,80]
l2=[50,100,150,200]
print(common_ele_list(l1,l2))

