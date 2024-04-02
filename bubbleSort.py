import sys

n = int(input("Enter the limit: "))

arr = list(map(int, input("Enter the elements: ").split()))

numSwap = 0
for i in range(n):
    numberOfSwaps = 0
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            numberOfSwaps += 1
    if numberOfSwaps == 0:
        break
    else:
        numSwap += numberOfSwaps

print("Array is sorted in %d swaps." % (numSwap))
print("First Element: %d" % (arr[0]))
print("Last Element: %d" % (arr[n - 1]))
print("The Sorted array is: %d"%(arr(i)))
