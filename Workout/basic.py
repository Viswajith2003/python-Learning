# print("Hello world");

# input read

# a=int(input("Enter the 1st number:"));
# b=int(input("Enter the 2nd number:"));
# print(type(a+b));


#arithematic opern

# x,y,z="viswa","jithu","god";
# print(x)
# print(y)
# print(z)
# a=10
# print(a==10 or a<5)
# print(a==10 and a<5)
# print(13 + 7);


# String manipulation

# str= "viswajith vp"
# print(str[0:5])
# print(len(str))
# print(str.strip())
# print(str.upper())
# print(str.replace("vp","mk"))
# a="learn"
# b="python"
# print(a+b)
# name ="Viswa"
# age =21
# str="My Name is {},and i am {} years hold"
# print(str.format(name,age))
#colr=["red","yellow","blue","green"]
# colr[3]="pink"
# for x in colr:
#     print(x)
# colr.remove(colr[0]);
# print(colr)


#set
#set={"red","yellow","blue","green"}
# print("pink" in set)
# print(len(set))
# set.add("pink")
# set.update(["anu","arun","amal"])
# set.remove("red")
# set.discard("yellow")
# print(set)


#Dictionary
# dict={
#     "Name":"Viswajith",
#     "Email":"viswajithviswa715@gmail.com",
#     "Phone":9072906576
# }
# a=dict["Email"]
# a=dict.get("Name")
# dict["Name"]="Viswa"  
# dict["Age"]=21
# for x in dict:
#     print(x)
#     print(dict[x])
# for x,y in dict.items():
#     print(x,y)
# dict.pop("Email")
# print(dict)



#IF..Else Statements
# a=10
# if a>0:
#     print("Positive Number");
# elif a<0:
#     print("Negative Number");
# else:
#     print("Zero")

# if(a>=0):
#     if(a>0):
#         print("positive number")
#     else:
#         print("Zero")
# else:
#     print("Negative number")

#a=10
# if a>5 and a<20:
#     print("Hello")



#While Loop
# i=1
# a="viswa"
# while i<=5:
#     print(a)
#     i +=1

#For Loop
# a=["red","blue","white","black"]
# for i in a:
#     print(i)

# for i in range(1,11):
#     print(i)


#Function
# def mesg():
#     print("Function in python")
# mesg()

# def msg(name):
#     print("Hello "+name)
# msg("Viswa")

# def sum(n1,n2):
#     s=n1+n2
#     print("The sum is :"+ str(s))
# sum(3,4)

# def find_square(num):
#     return num*num
# print(find_square(10))

# def recursion(n):
#     if n<=1:
#         return n
#     else:
#         return n+recursion(n-1)
# print(recursion(5))

# my_list = [1, 2, 3, 4, 5, 6]
# def even(x):
#     if x % 2 == 0:
#         return x
        
# s = filter(even, my_list)
# print(list(s))

# my_list = [1, 2, 3, 4, 5, 6]

# def even(x):
#     return x % 2 == 0

# filtered_list = filter(even, my_list)
# print(list(filtered_list))


 
#Inhertance

#Parent class
# class Person:
#     def __init__(self, name, contact):
#         self.name =name
#         self.contact=contact
#     def address(self):
#         print(self.name,self.contact)

# child class
# class Doctor(Person):
#     pass
# class Patient(Person):
#     pass
# doc1 =Doctor("john",1234)
# pat1 =Patient("Anil",98435) 

# doc1.address()
# pat1.address()


#Math Function
# a=min(12,4,45,2)   
# b=max(12,4,45,2)
# a=pow(2,3) # 2**3= 2*2*2= 8

# import math
# a=math.pi
# a=math.sqrt(9)
# a=math.gcd(8, 12) #greatest common device
# print(a)


#File Handling

# with open("/home/tufa15/Documents/PYTHON_pgms/sample.txt", "w") as f:
#     f.write("\nHello, Iam Viswa\n")
    
# with open("/home/tufa15/Documents/PYTHON_pgms/sample.txt", "a") as f:
#     f.write("\nHello, Iam Viswajith ,are u ok\n")

# with open("/home/tufa15/Documents/PYTHON_pgms/sample.txt", "r") as f:
#     read =f.read()
#     print(read)
#     f.close()

