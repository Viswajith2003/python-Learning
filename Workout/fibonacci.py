n=int(input("Enter the number: "))
f=0
s=1
print(f, s,end=" ")
for i in range(2,n+1):
    T=f+s
    f=s
    s=T
    print(T,end=" ")