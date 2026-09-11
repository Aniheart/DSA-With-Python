import math
x = int(input("enter: "))
class Solution:
  def isArmstrong(self,x):
    total_no = int(math.log10(abs(x)))+1
    original = x
    sum = 0
    while(x>0):
      ld = x%10
      sum = sum + ld**total_no
      x = x//10
    return original == sum
    
sol = Solution()
result = sol.isArmstrong(x)
print(result)

  
  