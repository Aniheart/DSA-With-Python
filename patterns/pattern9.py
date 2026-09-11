n = 3
for i in range(n):
  for j in range(i+1):
    print("*",end="")
  for k in range(2*(n-1),-1):
    print(" ",end="")
  for l in range(i+1):
    print("*",end="")
  print("")