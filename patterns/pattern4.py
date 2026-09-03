class Solution:
    def pattern4(self, n):
        for i in range(0,n,1):
            for j in range(0,n-1-i):
                print(" ", end="")
            for j in range(0,2*i+1):
                print("*",end="")
            for j in range(0,n-1-i):
                print(" ",end="")
            print("")

n = int(input("enter: "))
sol = Solution()
sol.pattern4(n)