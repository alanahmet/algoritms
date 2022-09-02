class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for k, r in count.items():
            if r > len(nums) // 2:
                return k
        return 0
