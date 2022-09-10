class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count, res = Counter(nums), 0
        for i in count.values():
            if i > 1:
                res += (i * (i - 1) // 2)
        return res
