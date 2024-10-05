# Write a program to find Leap year or not
# n=2024
# Output: Leap year
# n=2003
# Output: Not a Leap year

n=int(input("Enter the Number :"))
if n%4==0 and n%100!=0:
    print("Leap")
elif n%400==0:
    print("leap")
else:
    print("Not leap")