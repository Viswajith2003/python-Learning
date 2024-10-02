# Write a program to reverse a Number:
# input: 1225
# output: 5221

def RevNum(num):
    # last=num%10  #5
    # first=num//10 #122
    n=str(num)
    rev=n[::-1]
    return rev


num=1225
print(RevNum(num))
