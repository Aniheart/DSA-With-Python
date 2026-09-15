1# for i in range(n): by using loop
#   if(i>=n//2):
#     break
#   arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
arr = []
n = int(input())

while len(arr) < n:
    arr.extend(map(int, input().split()))

def reverse(i,n,arr):
  if(i>=n//2):
    return 
  arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
  reverse(i+1,n,arr)

reverse(i=0,n=n,arr=arr)
print(*arr)