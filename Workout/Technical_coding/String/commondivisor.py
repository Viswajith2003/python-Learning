

def commonDivisor(str1,str2):
    if (str1+str2)==(str2+str1):
        length=gcd(len(str1),len(str2))
        return str1[0:length]
                          
    return " "

str1="ababab"
str2="abab"
print(commonDivisor(str1,str2))
