class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        l, summ, ans = 0, 0, float('inf')

        for i, v in enumerate(nums):
            summ += v
            l += 1
            while summ >= target:
                ans = min(ans, l)
                summ -= nums[i - l + 1]
                l -= 1
            ans = ans - 1 if summ >= target else ans

        return ans if ans != float('inf') else 0
