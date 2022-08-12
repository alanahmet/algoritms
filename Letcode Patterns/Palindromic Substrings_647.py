class Solution:
    def countSubstrings(self, s: str) -> int:
        def findp(l: int, r: int):
            count: int = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count

        res = 0
        for i in range(len(s)):
            res += findp(i, i)
            res += findp(i, i + 1)

        return res
