n=int(input("Enter the number: "))
flag=0
for i in range(2,n):
  if n%2==0:
    flag=1
    break
if flag==1:
  print("This is not a prime number")
else:
  print("This is a prime number" )