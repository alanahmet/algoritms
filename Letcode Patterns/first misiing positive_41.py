class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        l = len(nums)
        for i in range(l):
            while 0 < nums[i] <= l and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, v in enumerate(nums):
            if not i + 1 == v:
                return i + 1
        return l + 1
