class Solution:
    def longestPalindrome(self, s: str) -> int:
        mid, count, ans = False, Counter(s), 0

        for v, c in count.items():
            if c % 2 == 1:
                if c > 1:
                    ans += (c - 1)
                if not mid:
                    ans += 1
                    mid = True
            else:
                ans += c

        return ans