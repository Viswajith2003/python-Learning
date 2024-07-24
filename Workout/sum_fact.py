class Solution:
   
    def factorial(self,n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact


    def sum_fact(self,n):
        
        sum=0
        org=n
        
        while n>0:
            digit=n%10
            f=self.factorial(digit)
            sum=sum+f
            n=n//10

        if sum==org:
            return "perfect"
        else:
            return "Not perfect"
    


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sum_fact(N))   
