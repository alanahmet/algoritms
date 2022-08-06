class Solution:
    def rob(self, nums: [int]) -> int:
        t1, t2 = 0, 0
        for i in nums:
            temp = max(t1 + i, t2)
            t1, t2 = t2, temp
        return t2
