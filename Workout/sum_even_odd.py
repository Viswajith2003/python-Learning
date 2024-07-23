#sum of odd and even numbers

def sum_odd_even(n):
  n=int(n)
  even_sum=0
  odd_sum=0
  for i in range(1,n+1):
    if i%2==0:
      even_sum=even_sum+i
    else:
      odd_sum=odd_sum+i
  return even_sum,odd_sum



num=int(input("Enter the number: "))
even,odd=sum_odd_even(num)
print(odd,even)