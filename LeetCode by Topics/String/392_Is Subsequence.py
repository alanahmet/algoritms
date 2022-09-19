class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps, pt = 0, 0

        while ps < len(s) and pt < len(t):
            while pt < len(t) and s[ps] != t[pt]:
                pt += 1
            ps += 1
            pt += 1

        return ps == len(s) and pt <= len(t)