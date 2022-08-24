class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2:
            return False
        dp = {0}
        target = nums_sum / 2

        for i in reversed(nums):
            nextDP = set()
            for j in dp:
                if j + i == target:
                    return True
                nextDP.add(j + i)
                nextDP.add(j)
            dp = nextDP
        return target in dp
