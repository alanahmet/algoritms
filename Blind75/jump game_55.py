class Solution:
    def canJump(self, nums: [int]) -> bool:
        if len(nums) == 0:
            return False
        j = 0
        for i in range(0, len(nums)):
            if i + 1 == len(nums):
                return True
            j = max(j - 1, nums[i])
            if j < 1:
                return False
        return True


print(Solution().canJump([0]))
