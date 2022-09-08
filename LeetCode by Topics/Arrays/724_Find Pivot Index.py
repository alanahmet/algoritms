class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lR = [nums[0]] * len(nums)  # left to right sum
        for i in range(1, len(nums)):
            lR[i] = lR[i - 1] + nums[i]
        for i in reversed(range(len(nums) - 1)):
            nums[i] += nums[i + 1]
        for i in range(len(nums)):
            if nums[i] == lR[i]:
                return i
        return -1
