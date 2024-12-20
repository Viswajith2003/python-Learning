def vowels(s):
    vowel=["A","E","I","O","U","a","e","i","o","u"]
    res=[]
    for i in range(len(s)):
        if s[i] in vowel:
            res.append(s[i])
    rev=res[::-1]
    return rev
    
                
s="Leetcode"
print(vowels(s))