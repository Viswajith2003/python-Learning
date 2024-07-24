def sum_of_digits(n):
    sum =0
    org=n
    while n>0:
      digit=n%10
      cube=digit**3
      sum=sum+cube
      n=n//10
    if org==sum:
        return 1
    else:
        return 0
    # return sum



num = int(input("Enter a number: "))
print("Sum of cube of digits:", sum_of_digits(num))
