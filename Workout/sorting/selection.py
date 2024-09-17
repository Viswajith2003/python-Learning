def selectionSort(n):
    for i in range(len(n)):
        curr_min=i
        for j in range(i+1,len(n)):
            if n[curr_min]>n[j]:
                curr_min=j
        n[i],n[curr_min]=n[curr_min],n[i]


arr=[5,3,4,2,6,1]
selectionSort(arr)
print(arr)