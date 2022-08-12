class Solution:
    def canJump(self, nums: [int]) -> bool:
        mj = nums[0]
        for i in nums:
            if mj == 0:
                return False
            mj = max(mj - 1, i)
        return True