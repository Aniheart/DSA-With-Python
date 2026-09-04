class Solution:
  def pattern(self,n):
    for i in range(2*n-1):
        stars = i+1
        if (i>=n):
          stars = 2*n-i-1
        for j in range(stars):
            print("*", end="")
        print(end="\n")

      
n = int(input("Enter: "))
sol = Solution()
sol.pattern(n)