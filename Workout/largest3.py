a, b, c = map(int, input("Enter the 3 numbers separated by spaces: ").split())

if(a>b and a>c):
  print(f"{a} is the largest number")
elif(b>a and b>c):
  print(f"{b} is the largest number")
else:
  print(f"{c} is the largest number")