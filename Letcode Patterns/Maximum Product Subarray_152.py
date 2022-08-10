class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, prevMin, prevMax = nums[0], nums[0], nums[0]

        for i in nums[1:]:
            mini, maxi = prevMin * i, prevMax * i
            prevMin = min(mini, maxi, i)
            prevMax = max(mini, maxi, i)
            res = max(res, prevMax)

        return res
