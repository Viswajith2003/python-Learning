def insertionSort(n):
  for i in range(1,len(n)):
    j=i
    while n[j-1]>n[j] and j>0:
      n[j-1],n[j]=n[j],n[j-1]
      j=j-1
  

arr=[2,6,5,1,3,4]
insertionSort(arr)
print(arr)