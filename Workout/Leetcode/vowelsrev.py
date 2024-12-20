def vowels(s):
    l=0
    r=len(s)-1
    vowel=["A","E","I","O","U","a","e","i","o","u"]
    s=list(s)
    while l<r:
        if s[l] not in vowel:
            l+=1
            continue

        if s[r] not in vowel:
            r-=1
            continue

        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1

    return "".join(s)


        
        

    
                
s="Leetcode"
print(vowels(s))