class Solution:
    def rob(self, nums: [int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        total_1, total_2 = 0, 0
        for i in nums[1:-1]:
            temp = max(total_1 + i, total_2)
            total_1 = total_2
            total_2 = temp
        return total_2


Sol = Solution()
sol = Sol.rob([1, 2, 1, 0])
print(sol)
