class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, farthest, end = 0, 0, 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:
                ans += 1
                end = farthest

        return ans
