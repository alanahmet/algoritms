class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        num_set = set(nums)
        for i in range(1, len(nums) + 2):
            print(i)
            if i not in num_set:
                return i
print(Solution().firstMissingPositive([1]))