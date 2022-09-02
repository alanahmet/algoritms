class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, maxCount, count, l = 0, 0, Counter(), 0

        for i, v in enumerate(s):
            count[v] += 1
            maxCount = max(maxCount, count[v])
            while maxCount + k < i - l + 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, i - l + 1)
        return ans
