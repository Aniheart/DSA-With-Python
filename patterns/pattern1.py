class Solution:
    def pattern1(self, n):
        for i in range(0,n,1):
            for j in range(0,n,1):
                print("*", end="")
            print(end="\n")

sol = Solution()
sol.pattern1(1)