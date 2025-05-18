n=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum+=i
print(sum)


# n=25
# The divisors of 25 are 1,5,25 .Their sum is 31 .

# n=20
# The divisors of 20 are 1,2,4,5,10,20 .Their sum is 42 .

# n=6
# The divisors of 6 are 1,2,3,6 .Their sum is 12.