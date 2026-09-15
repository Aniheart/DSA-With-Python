def name(i,n):
  if(i>n):
    return
  print("Aniket")
  name(i+1,n)
  
n = int(input())
name(1,n)