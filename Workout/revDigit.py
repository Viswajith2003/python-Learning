n=int(input("Enter the Number: "))
rev=0
while(n>0):
    last=n%10        #Get the last digit
    rev=rev*10+last  
    n=int(n/10)      #Remove the last digit
print(rev)

