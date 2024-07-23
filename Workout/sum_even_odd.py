#sum of odd and even numbers

def sum_odd_even(n):
  sum=0
  n=int(n)
  for i in range(n):
    sum=sum+i
  return(sum)



num=int(input("Enter the number: "))
print(sum_odd_even(num))