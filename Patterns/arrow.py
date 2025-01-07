n=5 
for i in range(n):
  for j in range(i+1):
    print(' ',end=' ')
  for k in range(n):
    print('*',end=' ')
  print()
for l in range(n-1):
  for m in range(n-l-1):
    print(' ',end=' ')
  for o in range(n):
    print('*',end=' ')
  print()