def sum_of_digits(n):
    sum =0
    for i in range(n):
      
      digit=n%10
      cube=digit**3
      sum=sum+cube
      n=n//10
      # if sum==n:
      #   return "yes"
      # else:
      #   return "no"
    return sum



num = int(input("Enter a number: "))
print("Sum of square of digits:", sum_of_digits(num))
