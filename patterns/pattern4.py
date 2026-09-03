class Solution4:
    def pattern4(self, n):
        for i in range(0,n,1):
            for j in range(0,n-1-i):
                print(" ", end="")
            for j in range(0,2*i+1):
                print("*",end="")
            for j in range(0,n-1-i):
                print(" ",end="")
            print("")

if __name__ == "__main__":
    n = int(input("enter: "))
    sol = Solution4()
    sol.pattern4(n)