n=int(input("Enter the number:"))

def isPrime(num):
    if num<2:
        return False;
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False;
    return True;

def prime_upto_n(n):
    for i in range(2,n+1):
        if isPrime(i):
            print(i)

prime_upto_n(n);

