class Solution:
    def fib(self, n: int) -> int:
        return F(n)
memo = {}
def F(n):
    if(n<=1):
        return n
    if n in memo:
        return memo[n]
    memo[n] = F(n-1) + F(n-2)
    return memo[n]

obj = Solution()
n = int(input())
answer = obj.fib(n)

print(answer)
        