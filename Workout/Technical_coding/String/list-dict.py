def listTodict():
    keys = [1, 2, 3, 4]
    values = ["red", "blue", "yellow", "green"]
    return dict(zip(keys, values))

s = listTodict()

def dictTotuple(s):
    return list(s.items())

print(dictTotuple(s))
