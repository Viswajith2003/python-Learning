import math

def commonDivisor(str1,str2):
    if (str1+str2)!=(str2+str1):
        return " "
    length=math.gcd(len(str1),len(str2))
    return str1[0:length]
                          

str1="abaaba"
str2="aba"
print(commonDivisor(str1,str2))

