class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        len_s = len(s)
        for i in range((len(s))):
            l, r = i, i
            while r < len_s and l > -1 and s[l] == s[r]:
                total+=1
                r += 1
                l -= 1
            l, r = i, i + 1
            while r < len_s and l > -1 and s[l] == s[r]:
                total += 1
                r += 1
                l -= 1
        return total
print(Solution().countSubstrings("aaa"))