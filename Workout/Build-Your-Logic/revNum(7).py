# Write a program to reverse a Number:
# input: 1225
# output: 5221

def RevNum(num):
    rev=0
    while num != 0:
        last=num%10  #5
        rev=rev*10+last
        num=num//10 #122
    return rev

    # n=str(num)
    # rev=n[::-1]
    # return rev

num=1225
print(RevNum(num))
