Write a program to find sum of elements at even (index) positions after reversing a given array.
nums=[10,20,30,40,50,60]
Output=120

def RevevenSum(n):
    rev=n[::-1]
    sum=0
    for i in range(0,len(rev),2):
        sum+=rev[i]
    return sum


num=[10,20,30,40,50,60]
print(RevevenSum(num))