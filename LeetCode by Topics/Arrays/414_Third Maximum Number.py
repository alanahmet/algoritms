class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sett = set(nums)
        if len(sett) > 2:
            return sorted(list(sett))[-3]
        return max(nums)