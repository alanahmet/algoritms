class Solution(object):
    def productExceptSelf(self, nums):
        nums_len = len(nums)
        res = [1 for _ in range(nums_len)]
        forward, backword = 1, 1
        for i in range(nums_len):
            res[i] *= forward
            forward *= nums[i]
            res[nums_len - 1 - i] *= backword
            backword *= nums[nums_len - 1 - i]
        return res
