n=5 
for i in range(n):
  for j in range(i+1):
    print(' ',end=' ')
  for k in range(i,n):
    print('*',end=' ')
  for r in range(i+1,n):
    print('*',end=' ')
  print()