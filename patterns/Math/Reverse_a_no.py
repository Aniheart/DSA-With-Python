x = int(input("Enter:"))
class Solution:
    def reverse(self, x: int) -> int:
        rev_no = 0
        isNeg = False
        if(x<0):
            isNeg = True
            x = x * (-1)
        while(x>0):
            last_digit = x%10
            x = x//10
            if rev_no > (2**31 - 1) // 10:
                return 0

            if rev_no == (2**31 - 1) // 10 and last_digit > 7:
                return 0
            rev_no = (rev_no * 10) + last_digit

        if(isNeg): 
            return -rev_no
        elif rev_no < -2**31 or rev_no > 2**31 - 1:
            return 0
        else:
            return rev_no
sol = Solution()
print(sol.reverse(x))