import collections


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

print(Solution().topKFrequent([1,1,1,2,2], 2))