class Solution:
    def pattern6(self, n):
        for i in range(0,n): #0 1 2 3 4
            for j in range(0,n-i-1): # 5 4 3 2 1
                print("*",end="")
            print("")

n = int(input("enter: "))
sol = Solution()
sol.pattern6(n)