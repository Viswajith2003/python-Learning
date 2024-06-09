num=[]
count=0
n=int(input("Enter the limit: "))
for i in range(0,n+1):
    even=i%2
    if(even==0):
        num.append(i)
        count=count+even

print("The list are: ",num)
print("No of Elements: ",count)
    
        
        