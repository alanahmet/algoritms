class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        len_s = len(s)
        for i in range((len(s))):
            l, r = i, i
            while r < len_s and l > -1 and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = r - l + 1
                    res = s[l:r + 1]
                r += 1
                l -= 1
            l, r = i, i + 1
            while r < len_s and l > -1 and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = r - l + 1
                    res = s[l:r + 1]
                r += 1
                l -= 1
        return res


print(Solution().longestPalindrome("caba"))
