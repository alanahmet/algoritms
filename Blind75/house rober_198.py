class Solution:
    def rob(self, nums: [int]) -> int:
        total_1, total_2 = 0, 0
        for i in nums:
            temp = max(total_1 + i, total_2)
            total_1 = total_2
            total_2 = temp
        return total_2
