#show RegNo and Atte_per of students below 75persontage attentence

dict={}
n=int(input("Enter the no: of students: "))
for i in range(n):
    regNo=int(input("Enter the RegNo: of students: "))
    Atte_per=int(input("Enter the Atte_per of students: "))
    dict[regNo]=Atte_per

for key in dict.keys():
    if dict[key]<75:
        print(key, ":" ,dict[key])
    