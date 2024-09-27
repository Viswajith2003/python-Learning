dupliArr=[1,3,2,3,4,5,6,4,1,2]

def removeDupli(arr):
    org=[]
    repeat=[]
    for i in arr:
        if i not in org:
            org.append(i)
        elif i not in repeat:
            repeat.append(i)
    return org,repeat

org,repeat=removeDupli(dupliArr)

print("Non dulplicate array:",org)
print("dulplicate elements:",repeat)



