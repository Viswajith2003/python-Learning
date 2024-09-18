def selectionSort(n):
    for i in range(len(n)):
        cur_var=i
        for j in range(i+1,len(n)):
            if n[cur_var]>n[j]:
                cur_var=j
        n[i],n[cur_var]=n[cur_var],n[i]

arr=[5,3,2,6,4,1]
selectionSort(arr)
print(arr)