num=[]
count=0
n=int(input("Enter the limit: "))
for i in range(0,n+1):
    if i%2==0:
        num.append(i)
        count=count+1

print("The list are: ",num)
print("No of Elements: ",count)
    
        
        