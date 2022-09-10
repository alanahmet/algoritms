class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)

        maxVals = []
        # find element with max value
        maxFreq = max(count.values())
        if maxFreq == 1:
            return 1

        for n in count:
            if count[n] == maxFreq:
                maxVals.append(n)

        res = 50000
        for n in maxVals:
            l = nums.index(n)
            r = len(nums) - nums[::-1].index(n)
            res = min(res, r - l)
        return res