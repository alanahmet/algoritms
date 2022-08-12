class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp, lenLIS, res = {}, 0, 0

        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1

            for j in range(i + 1, len(nums)):

                if nums[j] > nums[i]:
                    lenght, count = dp[j]
                    if lenght + 1 > maxLen:
                        maxLen, maxCnt = lenght + 1, count
                    elif lenght + 1 == maxLen:
                        maxCnt += count

            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt

            dp[i] = [maxLen, maxCnt]

        return res
