words=["apple","ant","banana","berry"]
Grp={}
for item in words:
    first=item[0]
    Grp.setdefault(first,[]).append(item)
print(Grp)