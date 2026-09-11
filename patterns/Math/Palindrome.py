x = int(input("Enter: "))
class Solution:
    def isPalindrome(self, x: int) -> bool:
      dup = x
      rev_no = 0
      if(x>=0):
        while(x>0):
          last_digit = x%10
          rev_no = (rev_no * 10) + last_digit
          x = x//10
      if(rev_no == dup):
        return True
      else:
        return False
sol = Solution()
print(sol.isPalindrome(x))
        