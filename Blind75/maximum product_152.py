class Solution:
    def maxProduct(self, nums: [int]) -> int:
        currMax, currMin = 1, 1
        max_val = max(nums)
        for i in nums:
            tmp = currMax * i
            currMax = max(currMax*i, currMin*i, i)
            currMin = min(currMax*i, currMin*i, i)
            max_val = max(max_val,currMax)
        return max_val

Ex = Solution()
ex = Ex.maxProduct([2, 3, -2, 4])
print(ex)
