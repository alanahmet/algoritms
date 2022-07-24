class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        sol = [1] * (len(nums))
        sol[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    sol[i] = max(sol[i], 1 + sol[j])
        print(sol)
        return max(sol)
Sol = Solution()
sol = Sol.lengthOfLIS([1,3,6,7,9,4,10,5,6])
print(sol)

