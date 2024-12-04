# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


x=int(input("Enter the number:"))
rev=0
sign=-1

if x<0:
    sign=-1
    x=x*-1                         # Convert x to positive

while x>0:
    rem=x%10
    rev=rev*10+rem
    x=x//10

rev=rev*sign                       # Restore the sign after reversing the number

if not -2147483648<=rev<=2147483647:    # Check the bounds of a 32-bit integer
    print(0)
print(sign*rev)






