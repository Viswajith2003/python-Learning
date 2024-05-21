Colors=["Red","Blue","Yellow","Green"]

#Add a item to the end of the list (append,insert,extent)
Colors.append("pink");
print(Colors);

#Add "white to the 2nd index number of the list"
Colors.insert(2,"white");
print(Colors);

#Find the length of the list
a=len(Colors);
print(a);

#check if 'black' is in the list
print('black' in Colors);      #False