def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


def sum_fact(n):
    
    sum=0
    org=n
    
    while n>0:
      digit=n%10
      f=factorial(digit)
      sum=sum+f
      n=n//10
    return sum


num = int(input("Enter a number: "))
print("factoril is:", sum_fact(num))