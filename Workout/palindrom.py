def isPalindrom(str):
    for i in range(0,int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True

strs=input("Enter the string:")
val=isPalindrom(strs)
if val:
    print("This is palindrome")
else:
    print("Not palindrom")

    

   


