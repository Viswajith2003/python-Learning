n=int(input("Enter the number :"))
flag=0
if n<=1:
    print("Not prime")
for i in range(2,int(n/2)+1):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("Not prime")
else:
    print("Prime")
    
