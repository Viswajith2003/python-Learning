#digitSum + palindrome


n=int(input("Enter the Number :"))

n=abs(n)
sum=0

while n>0:
    sum=sum+n%10
    n=n//10
print(sum)

if sum==int(str(sum)[::-1]):
    print("palindrome")
else:
    print("Not Palindrome")

