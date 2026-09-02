class Solution:
    def pattern3(self, n):
        for i in range(1,n+1,1):
            for j in range(1,i+1):
                print(j, end="")
            print(end="\n")

n = int(input("enter: "))
sol = Solution()
sol.pattern3(n)