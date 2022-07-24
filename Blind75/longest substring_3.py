class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        p1 = 0
        res = 0

        for p2 in range(len(s)):
            while s[p2] in char_set:
                char_set.remove(s[p1])
                p1 += 1
            char_set.add(s[p2])
            res = max(res, p2 - p1 + 1)
        return res

print(Solution().lengthOfLongestSubstring("abcabcbb"))
