
# Given a number, reverse it and add it to itself unless it becomes a palindrome or return -1 if the number of iterations becomes more than 5. Return that palindrome number if it becomes a palindrome else returns -1.

# Examples :

# Input: n = 23
# Output: 55 
# Explanation: reverse(23) = 32,then 32+23 = 55 which is a palindrome. 
# Input: n = 73
# Output: 121
# Explanation: reverse(73) = 37,then 37+73 = 110 which is not a palindrome, again reverse(110)= 011, then 110+11 = 121 which is a palindrome.

class Solution:
    def isSumPalindrome (self, n):
        
        # code here 
        org=n
        if org==int(str(org)[::-1]):
            return org
            
        rev=int(str(n)[::-1])
        sum=org+rev
        
            
        for i in range(0,5):
            s=int(str(org)) + int(str(org)[::-1])
            if s==int(str(s)[::-1]): 
                return s  
            org=s
        return '-1'

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
# } Driver Code Ends