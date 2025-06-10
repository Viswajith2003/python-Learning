

def alternativeMerge(word1,word2):
    i,j=0,0
    res=[]
    while i<len(word1) and j<len(word2):
        res.append(word1[i])                    #['a', 'p', 'b', 'q', 'c', 'r']
        res.append(word2[j])
        i+=1
        j+=1
    # res.append(word1[i:])
    # res.append(word2[j:])
    return  "".join(res)                        #apbqcr
    




word1="abc"
word2="pqr"
print(alternativeMerge(word1,word2))