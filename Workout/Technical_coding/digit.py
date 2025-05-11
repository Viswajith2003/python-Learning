def sum(number):
    num_str=str(number)
    f_no=int(num_str[0])
    l_no=int(num_str[-1])

    total=f_no+l_no

    return total

number=int(input("Enter the number:"))
res=sum(number)
print("The sum is:",res)




