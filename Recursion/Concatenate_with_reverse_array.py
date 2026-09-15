class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums1 = nums.copy()
        size = len(nums)
        for i in range(size):
            if(i>=size//2):
                break
            nums[i], nums[size-i-1] = nums[size-i-1], nums[i]
        nums1.extend(nums)
        return nums1

nums =[1, 2, 3]
sol = Solution()
result = sol.concatWithReverse(nums)
print(*result)