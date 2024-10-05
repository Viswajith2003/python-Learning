# Write a program to find Fibonacci sequence 
# 0,1,1,2,3,5,8,13.....

n=int(input("Enter the number: "))
first,second=0,1
for i in range(n):
    print(first, "\t")
    first,second=second,first+second



    
