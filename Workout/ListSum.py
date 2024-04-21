# Sum of the list of elements

N=int(input("Enter the limit: "))
lst=[]
Sum=0

for i in range(N):
  num=int(input("Enter the numbers: "))
  lst.append(num)
  Sum=Sum+lst[i]
print(Sum)