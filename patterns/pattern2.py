class Solution:
    def pattern2(self, n):
        for i in range(0,n,1):
            for j in range(0,i+1,1):
                print("*", end="")
            print(end="\n")

n=int(input("enter: "))
sol = Solution()
sol.pattern2(n)