str=input("Enter the string:")
arr=[]
try:
    for i in range(len(str)):
        str[i]=str[len(str)-i-1]
        arr=str[i]
    print(arr)
except:
    print("Error occur")


