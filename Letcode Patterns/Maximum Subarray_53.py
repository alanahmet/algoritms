class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        curr_sum = 0
        max_sum = nums[0]

        for i in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += i
            max_sum = max(max_sum, curr_sum)
        return max_sum
