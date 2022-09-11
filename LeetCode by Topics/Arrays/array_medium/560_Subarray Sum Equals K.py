class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, prefix, count = 0, 0, Counter({0: 1})

        for num in nums:
            prefix += num
            ans += count[prefix - k]
            count[prefix] += 1

        return ans