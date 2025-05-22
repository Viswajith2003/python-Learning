def freq_wd():
    str=input("Enter the string:")
    words=str.split()
    d={}

    for i in words:
        if i not in d.keys():
            d[i]=0
        d[i]+=1
    print(d)

freq_wd()

# Sheena loves eating apple and mango. Her sister also loves eating apple and mango.
# {'Sheena': 1, 'loves': 2, 'eating': 2, 'apple': 2, 'and': 2, 'mango.': 2, 'Her': 1, 'sister': 1, 'also': 1}