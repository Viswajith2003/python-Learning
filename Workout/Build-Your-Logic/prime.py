
# flag=0
# if n<=1:
#     print("Not prime")
# for i in range(2,int(n/2)+1):
#     if n%i==0:
#         flag=1
#         break
# if flag==1:
#     print("Not prime")
# else:
#     print("Prime")

def prime(n):
    if n<2:
        return False
    for j in range(2,int(n/2)+1):
        if n%j==0:
            return False
    return True    

n=int(input("Enter the number :"))
for num in range(1,n+1):
    if prime(num):
        print(num, "\n")
    
