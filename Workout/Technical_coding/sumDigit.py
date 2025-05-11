n=int(input("Enter the number: "))
sum=0
while n>0:
    last=n%10
    sum=sum+last
    n=int(n/10)
print(sum)