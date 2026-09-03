class Solution:
    def pattern5(self, n):
        for i in range(0,n,1):
            for j in range(0,i):
                print(" ", end="")
            for j in range(0,2*n-(2*i+1)):
                print("*",end="")
            for j in range(0,i):
                print(" ",end="")
            print("")
if __name__ == "__main__":
    n = int(input("enter: "))
    sol = Solution()
    sol.pattern5(n)