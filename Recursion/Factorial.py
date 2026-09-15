n = int(input())
def factorial(n):
  if(n<1):
    return 1
  return n * factorial(n-1)
fact = factorial(n)
print(fact)

# Time complexity O(n)
# space complexity O(n) and if using a loop space complexity will be O(1)