class Solution:
    def rob(self, nums: [int]) -> int:
        def robprofit(s, f):
            t1, t2 = 0, 0
            for i in nums[s:f]:
                temp = max(t1 + i, t2)
                t1, t2 = t2, temp
            return t2

        if not nums:
            return 0
        if len(nums) < 2:
            return max(nums)

        return max(robprofit(0, len(nums) - 1), robprofit(1, len(nums)))
