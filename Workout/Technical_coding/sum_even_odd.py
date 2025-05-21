# #sum of odd and even numbers

def sum_of_evenNo(n):
  n=int(n)
  l=[]
  even_sum=0
  for i in range(1,n+1):
    if i%2==0:
      l.append(i)
      even_sum+=i
  return even_sum,l

n=int(input("Enter the number:"))
even,num=sum_of_evenNo(n)
print("The numbers are:",num)
print("sum of even numbers is:",even)






























# def sum_odd_even(n):
#   n=int(n)
#   even_sum=0
#   odd_sum=0
#   for i in range(1,n+1):
#     if i%2==0:
#       even_sum=even_sum+i
#     else:
#       odd_sum=odd_sum+i
#   return even_sum,odd_sum



# num=int(input("Enter the number: "))
# even,odd=sum_odd_even(num)
# print(odd,even)